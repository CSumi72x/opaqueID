from cryptography.fernet import Fernet
import base64
import hashlib


def create_envelope(oprf_output):

    key = base64.urlsafe_b64encode(
        hashlib.sha256(
            oprf_output.encode()
        ).digest()
    )


    cipher = Fernet(key)


    secret = "OPAQUE_SECRET"


    encrypted = cipher.encrypt(
        secret.encode()
    )


    return encrypted.decode()



def open_envelope(oprf_output, envelope):

    key = base64.urlsafe_b64encode(
        hashlib.sha256(
            oprf_output.encode()
        ).digest()
    )


    cipher = Fernet(key)


    decrypted = cipher.decrypt(
        envelope.encode()
    )


    return decrypted.decode()