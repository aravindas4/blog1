import uuid


def get_uuid():
    return str(uuid.uuid4()).upper()[:8]
