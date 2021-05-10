from os import environ

class Config:

    ##### Global Configuration #####

    ENV = environ.get("SKOB_AUTHZ_ENV", "production")

    DEBUG = int(environ.get("SKOB_AUTHZ_DEBUG", "0"))

    TESTING = int(environ.get("SKOB_AUTHZ_TESTING", "0"))

    ##### Database Configuration #####

    SQLALCHEMY_DATABASE_URI = environ.get("SKOB_AUTHZ_DATABASE_URI", None)

    SQLALCHEMY_TRACK_MODIFICATIONS = TESTING

    ##### User Configuration #####

    USER_DEFAULT_ROLE = environ.get("SKOB_AUTHZ_USER_DEFAULT_ROLE", "member")

    USER_DEFAULT_STATUS = environ.get("SKOB_AUTHZ_USER_DEFAULT_STATUS", "inactive")
