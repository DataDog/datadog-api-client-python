"""
Get a change request returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.change_management_api import ChangeManagementApi

configuration = Configuration()
configuration.unstable_operations["get_change_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChangeManagementApi(api_client)
    response = api_instance.get_change_request(
        change_request_id="change_request_id",
    )

    print(response)
