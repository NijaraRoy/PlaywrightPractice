from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page: Page):
    #iphone X Nokia Edge
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone = page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    nokia_edge = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_edge.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body").filter(has_text="iphone X")).to_have_count(1)

def test_child_window_handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_page = newPage_info.value
        text = child_page.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        print(words[1].strip().split(" ")[0])
        assert email == "mentor@rahulshettyacademy.com"