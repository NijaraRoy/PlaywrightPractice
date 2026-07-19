from playwright.sync_api import Page, expect


def test_hide_show_example(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


def test_alert_box_confirmation(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_placeholder("Enter Your Name").fill("Roy")
    page.get_by_role("button", name="Confirm").click()
    #site clears the name field once the confirm dialog is accepted
    expect(page.get_by_placeholder("Enter Your Name")).to_have_value("")


def test_mouse_hover_navigation(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()
    expect(page).to_have_url("https://rahulshettyacademy.com/AutomationPractice/#top")


def test_iframe_content(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")


def test_price_table_lookup(page: Page):
    #identify the price column, locate the "Rice" row, verify its price
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    price_col_val = None
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count() > 0:
            price_col_val = i
            break
    assert price_col_val is not None, "Price column not found in table headers"

    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(price_col_val)).to_have_text("37")
