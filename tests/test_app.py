import pytest
from typing import TYPE_CHECKING
from app import app
from flask import Flask

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture

@pytest.fixture
def client() -> Flask:
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_rules(client: Flask) -> None:
    """Test the /rules endpoint."""
    response = client.get('/rules')
    assert response.status_code == 200