from authz import db
from authz.config import Config
from authz.util import now, uuidgen

class User(db.Model):
    """
    User table.
    Possible role values: admin, service, member
    Possible status values: active, inactive, blocked, suspend
    Do not touch id value please.
    """
    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(32), index=True, default=Config.USER_DEFAULT_ROLE)
    register_at = db.Column(db.DateTime, default=now)
    last_active_at = db.Column(db.DateTime)
    last_failed_at = db.Column(db.DateTime)
    status = db.Column(db.String(16), index=True, default=Config.USER_DEFAULT_STATUS)

