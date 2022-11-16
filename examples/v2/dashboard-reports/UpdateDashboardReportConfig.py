"""
Update Dashboard Report returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_reports_api import DashboardReportsApi
from datadog_api_client.v2.model.dashboard_report_schedule import DashboardReportSchedule
from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType
from datadog_api_client.v2.model.dashboard_report_update_attributes import DashboardReportUpdateAttributes
from datadog_api_client.v2.model.dashboard_report_update_request import DashboardReportUpdateRequest
from datadog_api_client.v2.model.dashboard_report_update_request_data import DashboardReportUpdateRequestData

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

# there is a valid "dashboard_report" in the system
DASHBOARD_REPORT_DATA_ID = environ["DASHBOARD_REPORT_DATA_ID"]

body = DashboardReportUpdateRequest(
    data=DashboardReportUpdateRequestData(
        attributes=DashboardReportUpdateAttributes(
            schedule=DashboardReportSchedule(
                active=False,
            ),
            title="Summary of performance for Web Application Backend",
        ),
        id=DASHBOARD_REPORT_DATA_ID,
        type=DashboardReportType.DASHBOARD_REPORTS_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardReportsApi(api_client)
    response = api_instance.update_dashboard_report_config(
        dashboard_id=DASHBOARD_ID, report_uuid=DASHBOARD_REPORT_DATA_ID, body=body
    )

    print(response)
