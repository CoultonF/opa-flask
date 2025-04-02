import pytest
from tests.app import create_app

@pytest.fixture()
def app():
    app_return = create_app()
    yield app_return

@pytest.fixture
def test_client(app):
    """Test client for the Flask application."""
    with app.test_client() as client:
        yield client