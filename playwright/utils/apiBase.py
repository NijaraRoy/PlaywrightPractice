from playwright.sync_api import Playwright

orderPayload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}


class APIUtils:

    # Accept user_credentials here
    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        # Dynamic email and password from parameters
        response = api_request_context.post(
            url="api/ecom/auth/login",
            data={
                "userEmail": "roynijaraa@gmail.com",
                "userPassword": "Testing@123"
            }
        )
        assert response.ok
        print(response.json())
        resBody = response.json()
        return resBody["token"]

    # Accept user_credentials here
    def create_order(self, playwright: Playwright):
        # Pass user_credentials along to getToken
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            url="/api/ecom/order/create-order",
            data=orderPayload,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )
        print(response.json())
        response_body = response.json()
        orderID = response_body["orders"][0]
        return orderID