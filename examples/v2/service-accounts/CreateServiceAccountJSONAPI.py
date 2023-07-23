"""
Create a service account returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.service_account_create_request import ServiceAccountCreateRequestJSON

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = ServiceAccountCreateRequestJSON(
    name="Test API Client",
    email="Example-Service-Account@datadoghq.com",
    service_account=True,
    roles=["string"],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account(body=body)

    print(response)
