import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
from utils.apiBaseFramework import APIUtils

#json file -> util-> access into test
with open('data\credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_cred_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_cred_list)
def test_e2e_web_api(playwright: Playwright, browser_instance, user_credentials):
    userEmail = user_credentials["user_email"]
    userPassword = user_credentials["user_password"]

    #create order --> orderId
    api_utils = APIUtils()
    orderID = api_utils.create_order(playwright, user_credentials)
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    dashboard_page = login_page.login(userEmail, userPassword)
    order_history_page = dashboard_page.select_orders_nav_link()
    order_details_page = order_history_page.selectOrder(orderID)
    order_details_page.verifyOrderMessage()
