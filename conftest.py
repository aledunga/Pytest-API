import json
import os
import pytest
import requests

BASE_URL = {
    "SANDBOX": {
        "external": "https://reqres.in",
        "internal_workflow": "https://reqres.in"},
    "STAGING": {
        "external": "https://reqres.in",
        "internal_workflow": "https://reqres.in"}
}


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        dest="env",
        default="STAGING",
        choices=("STAGING", "SANDBOX"),
        help="The environment for the application under test."
    )


@pytest.fixture(scope="session")
def env(request):
    """
    E.g.: SANDBOX, STAGING.
    :param request:
    :return: The environment for the application under test.
    """
    e = request.config.getoption("env")
    return e.upper()


@pytest.fixture(scope="session")
def base_url(env):
    """
    E.g. https://dummy.restapiexample.com
    :param env:
    :return: The API base URL corresponding to the given environment.
    """
    return BASE_URL[env]["external"]

@pytest.fixture(scope="session")
def list_users_url_v1(base_url):
    """
    E.g. https://dummy.restapiexample.com/api/v1/employees
    :param base_url:
    :return: The endpoint used by the API clients for order creation via workflow (v3).
    """
    return base_url + "/api/users?page=2"

@pytest.fixture(scope="session")
def single_user_url_v1(base_url):
    """
    E.g. https://dummy.restapiexample.com/api/v1/employees
    :param base_url:
    :return: The endpoint used by the API clients for order creation via workflow (v3).
    """
    return base_url + "/api/users/2"

@pytest.fixture(scope="session")
def single_user_not_found_url_v1(base_url):
    """
    E.g. https://dummy.restapiexample.com/api/v1/employees
    :param base_url:
    :return: The endpoint used by the API clients for order creation via workflow (v3).
    """
    return base_url + "/api/users/23"

@pytest.fixture(scope="session")
def create_user_url_v1(base_url):
    """
    E.g. https://dummy.restapiexample.com/api/v1/employees
    :param base_url:
    :return: The endpoint used by the API clients for order creation via workflow (v3).
    """
    return base_url + "/api/users"


@pytest.fixture(scope='session')
def no_auth_headers():
    """
    :return: The headers usually used for successful requests, but without the authorization token.
    """
    return {"Accept": "application/json", 'Content-Type': 'application/json'}
