"""
List shared dashboards for a dashboard returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_sharing_api import DashboardSharingApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_shared_dashboards_by_dashboard_id"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardSharingApi(api_client)
    response = api_instance.list_shared_dashboards_by_dashboard_id(
        dashboard_id="abc-def-ghi",
    )

    print(response)
