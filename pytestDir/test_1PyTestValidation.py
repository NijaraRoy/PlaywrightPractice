import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondwork function instance")
    yield
    print("tear down validation")

@pytest.mark.smoke
def test_initial_check(preWork, secondWork):
    print("This is the first test")
    assert preWork=="pass"

@pytest.mark.skip
def test_second_check(preSetupWork, secondWork):
    print("This is the second test")