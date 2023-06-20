"""
Update Fastly account returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi
from datadog_api_client.v2.model.fastly_account_update_request import FastlyAccountUpdateRequestJSON

# there is a valid "fastly_account" in the system
FASTLY_ACCOUNT_DATA_ID = environ["FASTLY_ACCOUNT_DATA_ID"]

body = FastlyAccountUpdateRequestJSON(
    api_key="update-secret",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.update_fastly_account(account_id=FASTLY_ACCOUNT_DATA_ID, body=body)

    print(response)
