"""
Schedule maintenance returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_maintenance_request import CreateMaintenanceRequest
from datadog_api_client.v2.model.create_maintenance_request_data import CreateMaintenanceRequestData
from datadog_api_client.v2.model.create_maintenance_request_data_attributes import (
    CreateMaintenanceRequestDataAttributes,
)
from datadog_api_client.v2.model.create_maintenance_request_data_attributes_components_affected_items import (
    CreateMaintenanceRequestDataAttributesComponentsAffectedItems,
)
from datadog_api_client.v2.model.patch_maintenance_request_data_attributes_components_affected_items_status import (
    PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus,
)
from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = CreateMaintenanceRequest(
    data=CreateMaintenanceRequestData(
        attributes=CreateMaintenanceRequestDataAttributes(
            completed_date=datetime(2026, 2, 18, 19, 51, 13, 332360, tzinfo=tzutc()),
            completed_description="We have completed maintenance on the API to improve performance.",
            components_affected=[
                CreateMaintenanceRequestDataAttributesComponentsAffectedItems(
                    id=UUID("1234abcd-12ab-34cd-56ef-123456abcdef"),
                    status=PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus.OPERATIONAL,
                ),
            ],
            in_progress_description="We are currently performing maintenance on the API to improve performance.",
            scheduled_description="We will be performing maintenance on the API to improve performance.",
            start_date=datetime(2026, 2, 18, 19, 21, 13, 332360, tzinfo=tzutc()),
            title="API Maintenance",
        ),
        type=PatchMaintenanceRequestDataType.MAINTENANCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_maintenance(page_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
