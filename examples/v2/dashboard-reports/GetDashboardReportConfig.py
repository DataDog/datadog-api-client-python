"""
Get a Dashboard Report returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_reports_api import DashboardReportsApi

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

# there is a valid "dashboard_report" in the system
DASHBOARD_REPORT_DATA_ID = environ["DASHBOARD_REPORT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardReportsApi(api_client)
    response = api_instance.get_dashboard_report_config(
        dashboard_id=DASHBOARD_ID,
        report_uuid=DASHBOARD_REPORT_DATA_ID,
    )

    print(response)
