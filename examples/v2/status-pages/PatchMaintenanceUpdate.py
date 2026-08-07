"""
Edit maintenance update returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_maintenance_update_request import PatchMaintenanceUpdateRequest
from datadog_api_client.v2.model.patch_maintenance_update_request_data import PatchMaintenanceUpdateRequestData
from datadog_api_client.v2.model.patch_maintenance_update_request_data_attributes import (
    PatchMaintenanceUpdateRequestDataAttributes,
)
from datadog_api_client.v2.model.patch_maintenance_update_request_data_type import PatchMaintenanceUpdateRequestDataType
from uuid import UUID

body = PatchMaintenanceUpdateRequest(
    data=PatchMaintenanceUpdateRequestData(
        attributes=PatchMaintenanceUpdateRequestDataAttributes(
            description="We have completed maintenance on the API to improve performance.",
        ),
        id="00000000-0000-0000-0000-000000000000",
        type=PatchMaintenanceUpdateRequestDataType.MAINTENANCE_UPDATES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.patch_maintenance_update(
        page_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        maintenance_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        update_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        body=body,
    )

    print(response)
