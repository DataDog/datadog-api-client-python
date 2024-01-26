"""
Create a new API returns "API created successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

configuration = Configuration()
configuration.unstable_operations["create_open_api"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.create_open_api(
        openapi_spec_file=open("openapi-spec.yaml", "rb"),
    )

    print(response)
