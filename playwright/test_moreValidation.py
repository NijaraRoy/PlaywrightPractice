import time

from playwright.sync_api import Page, expect


def test_uichecks(page: Page):
    #hide display placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alert box
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    #mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()

    #frameHandling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")

    #Check price tag
    #identify the price column
    #identify rice column
    # extract the price of rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count() > 0:
            price_col_val = i
            print(f"Price column value is {price_col_val}")
            break
    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(price_col_val)).to_have_text("37")

