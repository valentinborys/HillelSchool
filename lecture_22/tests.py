import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('test_search.log')
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


@pytest.fixture(scope='class')
def get_token():
    response = requests.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth('test_user', 'test_pass'))
    assert response.status_code == 200
    token = response.json().get('access_token')
    return token



@pytest.mark.parametrize("sort_by, limit", [
    (None, 2),
    ("brand", None),
    ("year", 5),
    ("engine_volume", 3),
    ("price", 4),
    (None, None),
    ("brand", 10)
])


def test_get_cars(get_token, sort_by, limit):
    headers = {'Authorization': f'Bearer {get_token}'}
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    logger.info(f"Testing with parameters: sort_by={sort_by}, limit={limit}")

    response = requests.get(f"{BASE_URL}/cars", headers=headers, params=params)
    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.json()}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
