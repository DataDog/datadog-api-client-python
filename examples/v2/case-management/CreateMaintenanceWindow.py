"""
Create a maintenance window returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.maintenance_window_create import MaintenanceWindowCreate
from datadog_api_client.v2.model.maintenance_window_create_attributes import MaintenanceWindowCreateAttributes
from datadog_api_client.v2.model.maintenance_window_create_request import MaintenanceWindowCreateRequest
from datadog_api_client.v2.model.maintenance_window_resource_type import MaintenanceWindowResourceType
from datetime import datetime
from dateutil.tz import tzutc

body = MaintenanceWindowCreateRequest(
    data=MaintenanceWindowCreate(
        attributes=MaintenanceWindowCreateAttributes(
            end_at=datetime(2026, 6, 1, 6, 0, tzinfo=tzutc()),
            name="Weekly maintenance",
            query="project:SEC",
            start_at=datetime(2026, 6, 1, 0, 0, tzinfo=tzutc()),
        ),
        type=MaintenanceWindowResourceType.MAINTENANCE_WINDOW,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_maintenance_window"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_maintenance_window(body=body)

    print(response)
