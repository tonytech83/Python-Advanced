from hashlib import sha256
from canvas import frame


def clean_screen():
    """
    Clears screen and prepare frame for new view.
    """
    frame.delete("all")


def get_password_hash(password):
    """
    Transforms the password and store the hash.
    """
    hash_object = sha256(password.encode())

    return str(hash_object.hexdigest())
