import pytest
from playwright.sync_api import Page, expect

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}
#api->browser->content server->returns back response to browser->browser use response and create html

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

@pytest.mark.smoke
def test_network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("roynijaraa@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Testing@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
    expect(page.locator(".mt-4")).to_have_text("You have No Orders to show at this time. Please Visit Back Us")

