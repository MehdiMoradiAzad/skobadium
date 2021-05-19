class ControllerRule:

    __controllers = {
        "get_users": ["admin"],
        "get_user": ["admin", "member:user_id"],
        "update_user": ["admin", "member:user_id"],
        "delete_user": ["admin"]
    }

    def get_controller_roles(name):
        return ControllerRule._ControllerRule__controllers.get(name)
