import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("I globally setup browser instance")