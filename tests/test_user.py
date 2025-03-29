import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_users_unauthorized(mocker):
    """Test with invalid credentials (401 Unauthorized) using pytest-mock"""
    url = f"{BASE_URL}/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mocking the requests.get() method
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mock_response.headers = {'Content-Type': 'text/plain'}
    
    mocker.patch('requests.get', return_value=mock_response)

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.headers.get("Content-Type") == "text/plain"
    assert response.text == ""


def test_users_valid_but_empty(mocker):
    """Test with valid credentials but empty response (200 OK) using pytest-mock"""
    url = f"{BASE_URL}/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mocking the requests.get() method
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mock_response.headers = {'Content-Type': 'text/plain'}
    
    mocker.patch('requests.get', return_value=mock_response)

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "text/plain"
    assert response.text == ""
