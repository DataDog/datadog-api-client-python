"""
Get usage stats for a dashboard returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboards_api import DashboardsApi

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

configuration = Configuration()
configuration.unstable_operations["get_dashboard_usage"] = True
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.get_dashboard_usage(
        dashboard_id=DASHBOARD_ID,
    )

    print(response)
