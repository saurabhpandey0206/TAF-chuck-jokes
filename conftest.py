import pytest
import app

@pytest.fixture(scope="class")
def test_setup():
    pytest.chuck_jokes = app.ChuckNorris()
    yield
