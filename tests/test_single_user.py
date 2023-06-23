import json
from http import HTTPStatus

import requests
import re



# q: is it better to leave this as a function outside the class, or inside the class as a method?
# TODO: add a conftest.py under tests folder and move function isValid there
#TODO: put project on github + github actions
#TODO: add other endpoints tests : PUT, PATCH, DELETE
#TODO: parametrize some tests ( like users data )
#TODO: add endpoints with authentication tests

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


class TestSingleUser:

    def test_retrieve_single_user_valid_email(self, single_user_url_v1, no_auth_headers):
        user_url = f"{single_user_url_v1}"
        response = requests.get(url=user_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print(response_body["data"])
        assert isValid(response_body["data"]["email"])

    def test_retrieve_single_user_valid_id(self, single_user_url_v1, no_auth_headers):
        user_url = f"{single_user_url_v1}"
        response = requests.get(url=user_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print(response_body["data"])
        assert 2 == int(response_body["data"]["id"])

    def test_retrieve_single_user_valid_first_name(self, single_user_url_v1, no_auth_headers):
        user_url = f"{single_user_url_v1}"
        response = requests.get(url=user_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print(response_body["data"])
        assert "Janet" == response_body["data"]["first_name"]

    def test_retrieve_single_user_valid_last_name(self, single_user_url_v1, no_auth_headers):
        user_url = f"{single_user_url_v1}"
        response = requests.get(url=user_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print(response_body["data"])
        assert "Weaver" == response_body["data"]["last_name"]

    def test_retrieve_single_user_valid_avatar(self, single_user_url_v1, no_auth_headers):
        user_url = f"{single_user_url_v1}"
        response = requests.get(url=user_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print(response_body["data"])
        assert "https://reqres.in/img/faces" in response_body["data"]["avatar"]

    def test_retrieve_single_user_not_found(self, single_user_not_found_url_v1, no_auth_headers):
        user_url = f"{single_user_not_found_url_v1}"
        response = requests.get(url=user_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.NOT_FOUND

        response_body = response.json()
        print(response_body)
        assert len(response_body) is 0