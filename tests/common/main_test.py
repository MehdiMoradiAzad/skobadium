import pytest

from authz import db

def test_env(app):
    assert app.config.get("ENV") == "testing"

def test_database_name(app):
    with app.app_context():
        result = db.session.execute("SELECT DATABASE();").first()
        assert result[0] == "testing"
