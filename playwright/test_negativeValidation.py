import pytest
from playwright.sync_api import Page, Playwright, expect


@pytest.mark.negative
def test_invalid_login_stays_on_login_page(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("roynijaraa@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("WrongPassword123")
    page.get_by_role("button", name="Login").click()
    #login stays on the same page and does not reveal the ORDERS nav on failure
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_role("button", name="  ORDERS")).not_to_be_visible()


@pytest.mark.negative
def test_api_login_with_invalid_credentials_returns_400(playwright: Playwright):
    api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    response = api_request_context.post(
        url="api/ecom/auth/login",
        data={
            "userEmail": "roynijaraa@gmail.com",
            "userPassword": "WrongPassword123"
        }
    )
    assert response.status == 400
    assert response.json()["message"] == "Incorrect email or password."


@pytest.mark.negative
def test_api_order_lookup_without_token_returns_401(playwright: Playwright):
    api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    response = api_request_context.get(
        url="/api/ecom/order/get-orders-details?id=000000000000000000000000"
    )
    assert response.status == 401
    assert response.json()["message"] == "Access denied. No token provided."


@pytest.mark.negative
def test_api_order_lookup_with_unknown_id_returns_400(playwright: Playwright):
    api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
    login_response = api_request_context.post(
        url="api/ecom/auth/login",
        data={
            "userEmail": "roynijaraa@gmail.com",
            "userPassword": "Testing@123"
        }
    )
    assert login_response.ok
    token = login_response.json()["token"]

    response = api_request_context.get(
        url="/api/ecom/order/get-orders-details?id=000000000000000000000000",
        headers={"Authorization": token}
    )
    assert response.status == 400
    assert response.json()["message"] == "Order not found"
