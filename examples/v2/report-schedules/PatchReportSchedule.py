"""
Update a report schedule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.report_schedules_api import ReportSchedulesApi
from datadog_api_client.v2.model.report_schedule_delivery_format import ReportScheduleDeliveryFormat
from datadog_api_client.v2.model.report_schedule_patch_request import ReportSchedulePatchRequest
from datadog_api_client.v2.model.report_schedule_patch_request_attributes import ReportSchedulePatchRequestAttributes
from datadog_api_client.v2.model.report_schedule_patch_request_data import ReportSchedulePatchRequestData
from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable
from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType
from uuid import UUID

body = ReportSchedulePatchRequest(
    data=ReportSchedulePatchRequestData(
        attributes=ReportSchedulePatchRequestAttributes(
            delivery_format=ReportScheduleDeliveryFormat.PDF,
            description="Updated weekly summary of infrastructure health.",
            recipients=[
                "user@example.com",
                "slack:T01234567.C01234567.alerts",
                "teams:11111111-1111-1111-1111-111111111111|22222222-2222-2222-2222-222222222222|19:exampleChannelId@thread.tacv2",
            ],
            rrule="DTSTART;TZID=America/New_York:20260601T090000\nRRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0",
            tab_id=UUID("66666666-7777-8888-9999-000000000000"),
            template_variables=[
                ReportScheduleTemplateVariable(
                    name="env",
                    values=[
                        "prod",
                    ],
                ),
            ],
            timeframe="calendar_month",
            timezone="America/New_York",
            title="Weekly Infrastructure Report",
        ),
        type=ReportScheduleType.SCHEDULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["patch_report_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = ReportSchedulesApi(api_client)
    response = api_instance.patch_report_schedule(schedule_uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
