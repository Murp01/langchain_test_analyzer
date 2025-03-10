import pytest

def test_success():
    assert 1 + 1 == 2

def test_failure():
    assert 1 + 1 == 3

def test_api():
    response_status = 500  # Simulating API failure
    assert response_status == 200