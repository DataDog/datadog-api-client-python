"""
Get Fastly account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

# there is a valid "fastly_account" in the system
FASTLY_ACCOUNT_DATA_ID = environ["FASTLY_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.get_fastly_account(
        account_id=FASTLY_ACCOUNT_DATA_ID,
    )

    print(response)
