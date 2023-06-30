import json
from http import HTTPStatus

import requests

#TODO: add a test_data class with test data for assertions
#TODO: refine the conftest.py fixtures to make it easier to read/use
#TODO: add github actions
#TODO: add other endpoints tests : PUT, PATCH, DELETE
#TODO: parametrize some tests ( like users data )
#TODO: add endpoints with authentication tests

class TestSingleUser:

    def test_retrieve_single_user_valid_email(self, single_user_url_v1, no_auth_headers, is_single_email_valid):
        user_url = f"{single_user_url_v1}"
        response = requests.get(url=user_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print(response_body["data"])
        assert is_single_email_valid

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