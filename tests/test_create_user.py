import json
from http import HTTPStatus

import requests
import datetime


class TestCreateUser:

    def test_create_user_name(self, create_user_url_v1, no_auth_headers):
        user_url = f"{create_user_url_v1}"
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(url=user_url, headers=no_auth_headers, data=json.dumps(payload))
        assert response.status_code == HTTPStatus.CREATED

        response_body = response.json()
        print(response_body)
        assert "morpheus" in response_body["name"]

    def test_create_user_job(self, create_user_url_v1, no_auth_headers):
        user_url = f"{create_user_url_v1}"
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(url=user_url, headers=no_auth_headers, data=json.dumps(payload))
        assert response.status_code == HTTPStatus.CREATED

        response_body = response.json()
        print(response_body)
        assert "leader" in response_body["job"]

    def test_create_user_id(self, create_user_url_v1, no_auth_headers):
        user_url = f"{create_user_url_v1}"
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(url=user_url, headers=no_auth_headers, data=json.dumps(payload))
        assert response.status_code == HTTPStatus.CREATED

        response_body = response.json()
        print(response_body)
        assert len(response_body["id"]) > 0

    def test_create_user_created_at(self, create_user_url_v1, no_auth_headers):
        user_url = f"{create_user_url_v1}"
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(url=user_url, headers=no_auth_headers, data=json.dumps(payload))
        assert response.status_code == HTTPStatus.CREATED

        response_body = response.json()
        print(response_body)
        assert datetime.date.today().strftime("%Y-%m-%d") in response_body["createdAt"]

