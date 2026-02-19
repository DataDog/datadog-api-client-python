"""
Delete a change request decision returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.change_management_api import ChangeManagementApi

configuration = Configuration()
configuration.unstable_operations["delete_change_request_decision"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChangeManagementApi(api_client)
    response = api_instance.delete_change_request_decision(
        change_request_id="change_request_id",
        decision_id="decision_id",
    )

    print(response)
