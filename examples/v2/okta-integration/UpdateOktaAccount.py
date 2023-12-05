"""
Update Okta account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi
from datadog_api_client.v2.model.okta_account_type import OktaAccountType
from datadog_api_client.v2.model.okta_account_update_request import OktaAccountUpdateRequest
from datadog_api_client.v2.model.okta_account_update_request_attributes import OktaAccountUpdateRequestAttributes
from datadog_api_client.v2.model.okta_account_update_request_data import OktaAccountUpdateRequestData

# there is a valid "okta_account" in the system
OKTA_ACCOUNT_DATA_ID = environ["OKTA_ACCOUNT_DATA_ID"]

body = OktaAccountUpdateRequest(
    data=OktaAccountUpdateRequestData(
        attributes=OktaAccountUpdateRequestAttributes(
            auth_method="oauth",
            domain="https://example.okta.com/",
            client_id="client_id",
            client_secret="client_secret",
        ),
        type=OktaAccountType.OKTA_ACCOUNTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.update_okta_account(account_id=OKTA_ACCOUNT_DATA_ID, body=body)

    print(response)
