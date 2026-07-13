from playwright.sync_api import Playwright

from playwright.sync_api import Page, expect


def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#chromium headless mode, 1 single context
def test_playwright_shortcut(page:Page):
    page.goto("https://rahulshetty.com")

def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #Incorrect username/password

def test_firefox_browser(playwright: Playwright):
     firefoxBrowser = playwright.firefox
     browser = firefoxBrowser.launch(headless=False)
     page = browser.new_page()
     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
     page.get_by_label("Username:").fill("rahulshettyacademy")
     page.get_by_label("Password:").fill("Learning@830$3mK")
     page.get_by_role("combobox").select_option("teach")
     page.locator("#terms").check()
     page.get_by_role("link", name="terms and conditions").click()
     page.get_by_role("button", name="Sign In").click()
     expect(page.get_by_text("Incorrect username/password.")).to_be_visible()







