import os
import hashlib
import base64


class OpaqueServer:


    def create_user_record(self, password: str):

        # Generate random salt
        salt = os.urandom(16)


        # Derive key from password
        key = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            100000
        )


        record = {
            "salt": base64.b64encode(salt).decode(),
            "verifier": base64.b64encode(key).decode()
        }


        return record



    def verify_password(self, password: str, record):

        salt = base64.b64decode(
            record["salt"]
        )


        stored_verifier = record["verifier"]


        key = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            100000
        )


        new_verifier = base64.b64encode(
            key
        ).decode()


        return new_verifier == stored_verifier