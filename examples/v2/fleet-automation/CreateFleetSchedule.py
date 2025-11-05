"""
Create a schedule returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_schedule_create import FleetScheduleCreate
from datadog_api_client.v2.model.fleet_schedule_create_attributes import FleetScheduleCreateAttributes
from datadog_api_client.v2.model.fleet_schedule_create_request import FleetScheduleCreateRequest
from datadog_api_client.v2.model.fleet_schedule_recurrence_rule import FleetScheduleRecurrenceRule
from datadog_api_client.v2.model.fleet_schedule_resource_type import FleetScheduleResourceType
from datadog_api_client.v2.model.fleet_schedule_status import FleetScheduleStatus

body = FleetScheduleCreateRequest(
    data=FleetScheduleCreate(
        attributes=FleetScheduleCreateAttributes(
            name="Weekly Production Agent Updates",
            query="env:prod AND service:web",
            rule=FleetScheduleRecurrenceRule(
                days_of_week=[
                    "Mon",
                    "Wed",
                    "Fri",
                ],
                maintenance_window_duration=1200,
                start_maintenance_window="02:00",
                timezone="America/New_York",
            ),
            status=FleetScheduleStatus.ACTIVE,
            version_to_latest=0,
        ),
        type=FleetScheduleResourceType.SCHEDULE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_fleet_schedule"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.create_fleet_schedule(body=body)

    print(response)
