from flask_restful import Resource
from authz.controller import UserController

class UserResource(Resource):

    def get(self, user_id=None):
        if user_id is None:
            return UserController.get_users()
        else:
            return UserController.get_user(user_id)

    def post(self):
        return UserController.create_user()

    def patch(self, user_id):
        return UserController.update_user(user_id)

    def delete(self, user_id):
        return UserController.delete_user(user_id)

