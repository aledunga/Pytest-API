Workflow API Tests
===============================

Workflow API Tests is a suite of end-to-end automated tests for testing the orders flow from OMS to CMS.

Running the Tests Locally
=========================

* System requirements:
  * python 3
  * pip

* Clone this repo

* Next, create and activate a virtual environment:

        virtualenv venv -p python3
        source venv/bin/activate

* Export the authentication token / API key into `AUTH_TOKEN` / `API_KEY` environment variable:

      export AUTH_TOKEN="Bearer eyJhb....F0pwnw"
      export API_KEY="1327....aae2"

* Install packages and project dependencies:

        cd venv
        pip install -r requirements.txt

* Run all tests or a certain API test, on a given environment:

        pytest -v -s --env SANDBOX
        pytest -v -s --env STAGING
        pytest -v -s --env SANDBOX -k test_create_user
        pytest -v --env SANDBOX -k test_create_user --html=SND_test_create_user_23Jun.html --self-contained-html