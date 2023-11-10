"""
Okta Public - Update account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi
from datadog_api_client.v2.model.okta_account import OktaAccount
from datadog_api_client.v2.model.okta_account_attributes import OktaAccountAttributes
from datadog_api_client.v2.model.okta_account_request import OktaAccountRequest
from datadog_api_client.v2.model.okta_account_type import OktaAccountType

body = OktaAccountRequest(
    data=OktaAccount(
        attributes=OktaAccountAttributes(
            auth_method="oauth",
            domain="https://example.okta.com/",
            name="Okta-Prod",
        ),
        id="f749daaf-682e-4208-a38d-c9b43162c609",
        type=OktaAccountType.OKTA_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.update_okta_account(account_id="account_id", body=body)

    print(response)
