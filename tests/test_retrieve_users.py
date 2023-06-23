import json
from http import HTTPStatus

import requests
import re

# q: is it better to leave this as a function outside the class, or inside the class as a method?

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


class TestRetrieveUsers:

    def test_retrieve_users_page_number(self, list_users_url_v1, no_auth_headers):
        users_url = f"{list_users_url_v1}"
        response = requests.get(url=users_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print("Response body: ", response_body)

        assert 2 == int(response_body["page"])

    def test_retrieve_users_per_page(self, list_users_url_v1, no_auth_headers):
        users_url = f"{list_users_url_v1}"
        response = requests.get(url=users_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print("Response body: ", response_body)

        assert 6 == int(response_body["per_page"])

    def test_retrieve_users_total(self, list_users_url_v1, no_auth_headers):
        users_url = f"{list_users_url_v1}"
        response = requests.get(url=users_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print("Response body: ", response_body)

        assert 12 == int(response_body["total"])

    def test_retrieve_users_total_pages(self, list_users_url_v1, no_auth_headers):
        users_url = f"{list_users_url_v1}"
        response = requests.get(url=users_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print("Response body: ", response_body)

        assert 2 == int(response_body["total_pages"])

    def test_retrieve_users_data(self, list_users_url_v1, no_auth_headers):
        users_url = f"{list_users_url_v1}"
        response = requests.get(url=users_url, headers=no_auth_headers)
        assert response.status_code == HTTPStatus.OK

        response_body = response.json()
        print("Response body: ", response_body)

        assert isValid(response_body["data"][0]["email"])
        assert 7 == int(response_body["data"][0]["id"])
        assert "Michael" == response_body["data"][0]["first_name"]
        assert "Lawson" == response_body["data"][0]["last_name"]
        assert "https://reqres.in/img/faces" in response_body["data"][0]["avatar"]

