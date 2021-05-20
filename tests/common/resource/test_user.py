import pytest

from json import dumps

@pytest.mark.parametrize(
        ("data", "headers", "status"),
        [
            ({}, {}, 415),
            ({}, {"Content-Type": "application/json"}, 400),
            ({"": ""}, {"Content-Type": "application/json"}, 400),
            ({"user": "test", "pass": "test"}, {"Content-Type": "application/json"}, 400),
            ({"username": "test", "password": "test", "key": "test"}, {"Content-Type": "application/json"}, 400),
            ({"username": "", "password": ""}, {"Content-Type": "application/json"}, 400),
            ({"username": "test-8", "password": "test"}, {"Content-Type": "application/json"}, 201),
            ({"username": "test-8", "password": "test"}, {"Content-Type": "application/json"}, 409)
        ]
)
def test_create_user(client, data, headers, status):
    result = client.post(
            "/users",
            data=dumps(data),
            headers=headers
    )
    assert result.status_code == status
