from flask import abort, request
from authz import db
from authz.model import User

class UserController:

    def create_user():
        if request.content_type != "application/json":
            abort(415)
        data = request.get_json()
        if len(data) != 2:
            abort(400)
        if "username" not in data or "password" not in data:
            abort(400)
        if not data["username"] or not data["password"]:
            abort(400)
        if type(data["username"]) is not str or type(data["password"]) is not str:
            abort(400)
        user = User.query.filter_by(username=data["username"]).first()
        if user is not None:
            abort(409)
        user = User(username=data["username"], password=data["password"])
        db.session.add(user)
        db.session.commit()

    def get_users():
        pass

    def get_user(user_id):
        pass

    def update_user(user_id):
        pass

    def delete_user(user_id):
        pass
