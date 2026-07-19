import pytest
from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

scenarios("features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('Place the itme order with {userEmail} and {userPassword}'))
def place_item_order(playwright, userEmail, userPassword, shared_data):
    user_credentials = {}
    user_credentials["user_email"] = userEmail
    user_credentials["user_password"] = userPassword
    api_utils = APIUtils()
    orderID = api_utils.create_order(playwright, user_credentials)
    shared_data["orderID"] = orderID

@given('the user is on landing page')
def user_on_the_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data["login_page"] = login_page

@when(parsers.parse("I login to portal with {userEmail} and {userPassword}"))
def login_to_portal(userEmail, userPassword, shared_data):
    login_page = shared_data["login_page"]
    dashboard_page = login_page.login(userEmail, userPassword)
    shared_data["dashboard_page"] = dashboard_page

@when("navigate to orders page")
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data["dashboard_page"]
    order_history_page = dashboard_page.select_orders_nav_link()
    shared_data["order_history_page"] = order_history_page


@when("select the orderId")
def select_order_id(shared_data):
    order_history_page = shared_data["order_history_page"]
    orderID = shared_data["orderID"]
    order_details_page = order_history_page.selectOrder(orderID)
    shared_data["order_details_page"] = order_details_page


@then("order message is successfully displayed")
def order_message_successfully_displayed(shared_data):
    order_details_page = shared_data["order_details_page"]
    order_details_page.verifyOrderMessage()


@then("the login page is still displayed")
def login_page_is_still_displayed(shared_data):
    login_page = shared_data["login_page"]
    expect(login_page.page.get_by_role("button", name="Login")).to_be_visible()
    expect(login_page.page.get_by_role("button", name="  ORDERS")).not_to_be_visible()