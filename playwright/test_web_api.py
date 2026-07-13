from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order --> orderId
    api_utils = APIUtils()
    orderID = api_utils.create_order(playwright)


    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("roynijaraa@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Testing@123")
    page.get_by_role("button", name="Login").click()

    #Order history --> order is present
    page.get_by_role("button", name="  ORDERS").click()
    row = page.locator("tr").filter(has_text=orderID)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()