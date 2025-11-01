"""
List connections returns "Successful response with list of connections" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi

configuration = Configuration()
configuration.unstable_operations["list_connections"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.list_connections(
        entity="users",
    )

    print(response)
