"""
Get Okta account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.okta_integration_api import OktaIntegrationApi

# there is a valid "okta_account" in the system
OKTA_ACCOUNT_DATA_ID = environ["OKTA_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OktaIntegrationApi(api_client)
    response = api_instance.get_okta_account(
        account_id=OKTA_ACCOUNT_DATA_ID,
    )

    print(response)
