"""
Get all invitations for a shared dashboard returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

# there is a valid "shared_dashboard" in the system
SHARED_DASHBOARD_TOKEN = environ["SHARED_DASHBOARD_TOKEN"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.get_public_dashboard_invitations(
        token=SHARED_DASHBOARD_TOKEN,
    )

    print(response)
