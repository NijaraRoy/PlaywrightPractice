from playwright.sync_api import Page, expect, Playwright

from utils.apiBase import APIUtils


#api->browser->content server->returns back response to browser->browser use response and create html

def intercept_request(route):
    route.continue_(
        url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0"
    )

def test_network2(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("roynijaraa@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Testing@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
    expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")

def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    get_token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject token to session local storage
    page.add_init_script(f"""localStorage.setItem('token', '{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
    page.get_by_role("button", name="View").first.click()

