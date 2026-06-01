"""
Get usage stats for all dashboards with viewed_before filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi

configuration = Configuration()
configuration.unstable_operations["list_dashboards_usage"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards_usage(
        filter_viewed_before="2025-04-26T00:00:00Z",
    )

    print(response)
