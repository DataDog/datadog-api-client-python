"""
Create backfilled maintenance returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_backfilled_maintenance_request import CreateBackfilledMaintenanceRequest
from datadog_api_client.v2.model.create_backfilled_maintenance_request_data import (
    CreateBackfilledMaintenanceRequestData,
)
from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_attributes import (
    CreateBackfilledMaintenanceRequestDataAttributes,
)
from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_attributes_updates_items import (
    CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems,
)
from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_attributes_updates_items_status import (
    CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus,
)
from datadog_api_client.v2.model.create_maintenance_request_data_attributes_components_affected_items import (
    CreateMaintenanceRequestDataAttributesComponentsAffectedItems,
)
from datadog_api_client.v2.model.patch_maintenance_request_data_attributes_components_affected_items_status import (
    PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus,
)
from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = environ[
    "STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"
]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = CreateBackfilledMaintenanceRequest(
    data=CreateBackfilledMaintenanceRequestData(
        attributes=CreateBackfilledMaintenanceRequestDataAttributes(
            title="Past Database Maintenance",
            updates=[
                CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems(
                    components_affected=[
                        CreateMaintenanceRequestDataAttributesComponentsAffectedItems(
                            id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                            status=PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus.MAINTENANCE,
                        ),
                    ],
                    description="Database maintenance is in progress.",
                    started_at=(datetime.now() + relativedelta(hours=-1)),
                    status=CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus.IN_PROGRESS,
                ),
                CreateBackfilledMaintenanceRequestDataAttributesUpdatesItems(
                    components_affected=[
                        CreateMaintenanceRequestDataAttributesComponentsAffectedItems(
                            id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                            status=PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus.OPERATIONAL,
                        ),
                    ],
                    description="Database maintenance has been completed successfully.",
                    started_at=datetime.now(),
                    status=CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus.COMPLETED,
                ),
            ],
        ),
        type=PatchMaintenanceRequestDataType.MAINTENANCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_backfilled_maintenance(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
