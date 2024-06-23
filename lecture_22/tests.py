# test_app.py
import pytest
import requests
import logging

BASE_URL = "http://127.0.0.1:5000"

logging.basicConfig(filename='test_search.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger()


@pytest.fixture(scope='class')
def auth():
    response = requests.post(f"{BASE_URL}/auth", json={"username": "user1", "password": "password1"})
    token = response.json().get("token")
    assert token, "Authentication failed"
    return {"Authorization": f"Bearer {token}"}


@pytest.mark.parametrize("sort_by, limit", [
    ("make", 2),
    ("model", 1),
    (None, 2),
    ("make", None),
    (None, None),
])
def test_get_cars(auth, sort_by, limit):
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit is not None:
        params['limit'] = limit

    response = requests.get(f"{BASE_URL}/cars", headers=auth, params=params)

    assert response.status_code == 200, f"Failed with status code {response.status_code}"

    cars = response.json()
    logger.info(f"Test params: sort_by={sort_by}, limit={limit} -> Response: {cars}")

    # Додаткові перевірки можна додати тут


if __name__ == "__main__":
    pytest.main(["-s", "test_app.py"])
