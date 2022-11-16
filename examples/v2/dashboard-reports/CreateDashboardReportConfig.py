"""
Create a new Dashboard Report returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dashboard_reports_api import DashboardReportsApi
from datadog_api_client.v2.model.dashboard_report_create import DashboardReportCreate
from datadog_api_client.v2.model.dashboard_report_create_attributes import DashboardReportCreateAttributes
from datadog_api_client.v2.model.dashboard_report_create_request import DashboardReportCreateRequest
from datadog_api_client.v2.model.dashboard_report_destination import DashboardReportDestination
from datadog_api_client.v2.model.dashboard_report_destination_email import DashboardReportDestinationEmail
from datadog_api_client.v2.model.dashboard_report_schedule import DashboardReportSchedule
from datadog_api_client.v2.model.dashboard_report_schedule_frequency import DashboardReportScheduleFrequency
from datadog_api_client.v2.model.dashboard_report_schedule_repeat_at import DashboardReportScheduleRepeatAt
from datadog_api_client.v2.model.dashboard_report_timeframe import DashboardReportTimeframe
from datadog_api_client.v2.model.dashboard_report_type import DashboardReportType

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

body = DashboardReportCreateRequest(
    data=DashboardReportCreate(
        attributes=DashboardReportCreateAttributes(
            description="This report summarizes the recent errors, latency, and uptime of our Web Application Backend.",
            destinations=DashboardReportDestination(
                email=DashboardReportDestinationEmail(
                    recipient_addresses=[
                        "jane.doe@example.com",
                    ],
                ),
            ),
            schedule=DashboardReportSchedule(
                active=True,
                frequency=DashboardReportScheduleFrequency.DASHBOARD_REPORT_SCHEDULE_FREQUENCY_1D,
                repeat_at=DashboardReportScheduleRepeatAt.DASHBOARD_REPORT_SCHEDULE_REPEAT_AT_13_30,
                repeat_on_day_of_month=None,
                repeat_on_day_of_week=None,
                timezone="America/New_York",
            ),
            timeframe=DashboardReportTimeframe.DASHBOARD_REPORT_TIMEFRAME_1W,
            title="Summary of recent stability and performance for Web Application Backend",
        ),
        type=DashboardReportType.DASHBOARD_REPORTS_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardReportsApi(api_client)
    response = api_instance.create_dashboard_report_config(dashboard_id=DASHBOARD_ID, body=body)

    print(response)
