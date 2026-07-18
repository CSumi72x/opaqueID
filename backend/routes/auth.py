from fastapi import APIRouter, Header

from schemas import UserRegister, UserLogin

from database import users_collection

from utils.jwt_handler import (
    create_access_token,
    verify_access_token
)

from opaque.oprf import (
    OPRFClient,
    OPRFServer
)

from opaque.envelope import (
    create_envelope,
    open_envelope
)


router = APIRouter()


# Persistent OPRF server
oprf_server = OPRFServer()



# ================= REGISTER =================

@router.post("/register")
async def register(user: UserRegister):

    # Check existing user

    existing_user = await users_collection.find_one(
        {
            "email": user.email
        }
    )


    if existing_user:

        return {
            "message": "Email already registered"
        }



    # Create OPRF client

    client = OPRFClient()



    # Blind password

    blinded_password = client.blind_password(
        user.password
    )



    # Server evaluation

    evaluated_password = oprf_server.evaluate(
        blinded_password
    )



    # Remove blinding

    oprf_result = client.unblind(
        evaluated_password
    )



    # Create envelope

    envelope = create_envelope(
        str(oprf_result)
    )



    # Store user

    user_data = {

        "username": user.username,

        "email": user.email,

        "envelope": envelope

    }


    await users_collection.insert_one(
        user_data
    )


    return {

        "message":
        "OPAQUE Registration Successful"

    }





# ================= LOGIN =================

@router.post("/login")
async def login(user: UserLogin):


    # Find user

    db_user = await users_collection.find_one(
        {
            "email": user.email
        }
    )



    if db_user is None:

        return {

            "message":
            "User not found"

        }



    try:


        # Create OPRF client

        client = OPRFClient()



        # Blind password

        blinded_password = client.blind_password(
            user.password
        )



        # Server evaluates

        evaluated_password = oprf_server.evaluate(
            blinded_password
        )



        # Unblind

        oprf_result = client.unblind(
            evaluated_password
        )



        # Open envelope

        secret = open_envelope(
            str(oprf_result),
            db_user["envelope"]
        )



        if secret != "OPAQUE_SECRET":

            return {

                "message":
                "Invalid Password"

            }




        # Create JWT

        token = create_access_token(

            {

                "username":
                db_user["username"],


                "email":
                db_user["email"]

            }

        )



        return {


            "message":
            "OPAQUE Login Successful",


            "access_token":
            token,


            "token_type":
            "bearer",


            "username":
            db_user["username"],


            "email":
            db_user["email"]

        }



    except Exception as e:

        print(e)

        return {

            "message":
            "Invalid Password"

        }





# ================= PROFILE =================


@router.get("/profile")
async def profile(
    authorization: str = Header(None)
):


    print(
        "AUTH HEADER:",
        authorization
    )


    if authorization is None:

        return {

            "message":
            "Token Missing"

        }



    token = authorization.replace(
        "Bearer ",
        ""
    )



    payload = verify_access_token(
        token
    )



    if payload is None:

        return {

            "message":
            "Invalid Token"

        }



    return {


        "username":
        payload["username"],


        "email":
        payload["email"]

    }