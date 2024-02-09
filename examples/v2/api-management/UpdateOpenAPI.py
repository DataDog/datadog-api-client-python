"""
Update an API returns "API updated successfully" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

# there is a valid "managed_api" in the system
MANAGED_API_DATA_ID = environ["MANAGED_API_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["update_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.update_open_api(
        id=MANAGED_API_DATA_ID,
        openapi_spec_file=open("openapi-spec.yaml", "rb"),
    )

    print(response)
