"""
Get Dashboard Reports for a Dashboard returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_reports_api import DashboardReportsApi

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardReportsApi(api_client)
    response = api_instance.get_dashboard_report_configs_list(
        dashboard_id=DASHBOARD_ID,
    )

    print(response)
