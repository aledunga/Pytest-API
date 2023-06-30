import pytest
import re
import requests


@pytest.fixture
def get_users_email(env, list_users_url_v1, no_auth_headers):
    users_url = f"{list_users_url_v1}"
    response = requests.get(url=users_url, headers=no_auth_headers)

    response_body = response.json()
    print("Response body: ", response_body)

    return response_body["data"][0]["email"]


@pytest.fixture
def get_single_user_email(env, single_user_url_v1, no_auth_headers):
    user_url = f"{single_user_url_v1}"
    response = requests.get(url=user_url, headers=no_auth_headers)

    response_body = response.json()
    print("Response body: ", response_body)

    return response_body["data"]["email"]


@pytest.fixture
def is_email_valid(get_users_email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, get_users_email):
        return True
    else:
        return False

@pytest.fixture
def is_single_email_valid(get_single_user_email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, get_single_user_email):
        return True
    else:
        return False
