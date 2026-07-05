import pytest

@pytest.fixture
def posts_data():
    return {
        "title": "POST",
        "body" : "contenido de POST",
        "userId":1
    }

@pytest.fixture
def users_data():
    return{
        "name": "Nonmbre Usuario",
        "username": "USRNAME",
        "email":"User@mail.com"
    }