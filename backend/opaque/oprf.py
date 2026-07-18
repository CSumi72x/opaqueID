import os
import hashlib
import secrets
from ecpy.curves import Curve


curve = Curve.get_curve("Ed25519")

KEY_FILE = "oprf_server.key"


def hash_to_curve(password):

    password_hash = hashlib.sha256(
        password.encode()
    ).digest()

    value = int.from_bytes(
        password_hash,
        "big"
    )

    point = curve.generator * (
        value % curve.order
    )

    return point


class OPRFServer:

    def __init__(self):

        # Load existing server key if available
        if os.path.exists(KEY_FILE):

            with open(KEY_FILE, "r") as file:

                self.secret_key = int(file.read())

            print("✅ Existing OPRF Server Key Loaded")

        else:

            # Generate new server key
            self.secret_key = secrets.randbelow(
                curve.order
            )

            with open(KEY_FILE, "w") as file:

                file.write(str(self.secret_key))

            print("✅ New OPRF Server Key Generated")


    def evaluate(self, blinded_point):

        return blinded_point * self.secret_key


class OPRFClient:

    def __init__(self):

        self.blind = secrets.randbelow(
            curve.order
        )


    def blind_password(self, password):

        point = hash_to_curve(password)

        blinded_point = (
            point * self.blind
        )

        return blinded_point


    def unblind(self, evaluated_point):

        inverse = pow(
            self.blind,
            -1,
            curve.order
        )

        result = (
            evaluated_point * inverse
        )

        return result