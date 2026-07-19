import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser slection"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="run browser_instance headless (default: headed, for local debugging)"
    )

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    if browser_name.lower() == "chrome":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name.lower() == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser_name: {browser_name}. Use 'chrome' or 'firefox'.")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

