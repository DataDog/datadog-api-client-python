"""
Delete connection returns "Connection deleted successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi

configuration = Configuration()
configuration.unstable_operations["delete_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    api_instance.delete_connection(
        id="connection-id-123",
        entity="users",
    )
