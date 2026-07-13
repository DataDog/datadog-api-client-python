"""
Print a report returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.report_schedules_api import ReportSchedulesApi
from datadog_api_client.v2.model.print_report_request import PrintReportRequest
from datadog_api_client.v2.model.print_report_request_attributes import PrintReportRequestAttributes
from datadog_api_client.v2.model.print_report_request_data import PrintReportRequestData
from datadog_api_client.v2.model.print_report_type import PrintReportType
from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable

body = PrintReportRequest(
    data=PrintReportRequestData(
        attributes=PrintReportRequestAttributes(
            from_ts=1780318800000,
            resource_id="abc-def-ghi",
            resource_type=ReportScheduleResourceType.DASHBOARD,
            template_variables=[
                ReportScheduleTemplateVariable(
                    name="env",
                    values=[
                        "prod",
                    ],
                ),
            ],
            timeframe="1w",
            timezone="America/New_York",
            to_ts=1780923600000,
        ),
        type=PrintReportType.REPORT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReportSchedulesApi(api_client)
    response = api_instance.print_report(body=body)

    print(response)
