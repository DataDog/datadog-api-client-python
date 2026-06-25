"""
Get report schedules for a resource returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.report_schedules_api import ReportSchedulesApi
from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReportSchedulesApi(api_client)
    response = api_instance.get_report_schedules_for_resource(
        resource_type=ReportScheduleResourceType.DASHBOARD,
        resource_id="resource_id",
    )

    print(response)
