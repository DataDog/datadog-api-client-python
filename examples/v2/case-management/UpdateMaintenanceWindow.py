"""
Update a maintenance window returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.maintenance_window_resource_type import MaintenanceWindowResourceType
from datadog_api_client.v2.model.maintenance_window_update import MaintenanceWindowUpdate
from datadog_api_client.v2.model.maintenance_window_update_attributes import MaintenanceWindowUpdateAttributes
from datadog_api_client.v2.model.maintenance_window_update_request import MaintenanceWindowUpdateRequest

body = MaintenanceWindowUpdateRequest(
    data=MaintenanceWindowUpdate(
        attributes=MaintenanceWindowUpdateAttributes(),
        type=MaintenanceWindowResourceType.MAINTENANCE_WINDOW,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_maintenance_window"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_maintenance_window(maintenance_window_id="maintenance_window_id", body=body)

    print(response)
