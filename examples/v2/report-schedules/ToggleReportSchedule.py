"""
Toggle a report schedule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.report_schedules_api import ReportSchedulesApi
from datadog_api_client.v2.model.report_schedule_status import ReportScheduleStatus
from datadog_api_client.v2.model.report_schedule_toggle_request import ReportScheduleToggleRequest
from datadog_api_client.v2.model.report_schedule_toggle_request_attributes import ReportScheduleToggleRequestAttributes
from datadog_api_client.v2.model.report_schedule_toggle_request_data import ReportScheduleToggleRequestData
from datadog_api_client.v2.model.report_schedule_type import ReportScheduleType
from uuid import UUID

body = ReportScheduleToggleRequest(
    data=ReportScheduleToggleRequestData(
        attributes=ReportScheduleToggleRequestAttributes(
            status=ReportScheduleStatus.ACTIVE,
        ),
        type=ReportScheduleType.SCHEDULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReportSchedulesApi(api_client)
    response = api_instance.toggle_report_schedule(
        schedule_uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
