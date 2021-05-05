from uuid import uuid4

def uuidgen():
    """
    Generate new UUID for resources id field in Database
    """
    return uuid4().hex
