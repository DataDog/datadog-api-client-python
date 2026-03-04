"""
Update maintenance returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_maintenance_request import PatchMaintenanceRequest
from datadog_api_client.v2.model.patch_maintenance_request_data import PatchMaintenanceRequestData
from datadog_api_client.v2.model.patch_maintenance_request_data_attributes import PatchMaintenanceRequestDataAttributes
from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

# there is a valid "maintenance" in the system
MAINTENANCE_DATA_ID = environ["MAINTENANCE_DATA_ID"]

body = PatchMaintenanceRequest(
    data=PatchMaintenanceRequestData(
        attributes=PatchMaintenanceRequestDataAttributes(
            scheduled_description="We will be performing maintenance on the API to improve performance for 40 minutes.",
            in_progress_description="We are currently performing maintenance on the API to improve performance for 40 minutes.",
        ),
        id=MAINTENANCE_DATA_ID,
        type=PatchMaintenanceRequestDataType.MAINTENANCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_maintenance(
        page_id=STATUS_PAGE_DATA_ID, maintenance_id=MAINTENANCE_DATA_ID, body=body
    )

    print(response)
