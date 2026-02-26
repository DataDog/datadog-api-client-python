"""
Create maintenance returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
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

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = environ[
    "STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"
]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = CreateMaintenanceRequest(
    data=CreateMaintenanceRequestData(
        attributes=CreateMaintenanceRequestDataAttributes(
            title="API Maintenance",
            scheduled_description="We will be performing maintenance on the API to improve performance.",
            in_progress_description="We are currently performing maintenance on the API to improve performance.",
            completed_description="We have completed maintenance on the API to improve performance.",
            start_date=(datetime.now() + relativedelta(hours=1)),
            completed_date=(datetime.now() + relativedelta(hours=2)),
            components_affected=[
                CreateMaintenanceRequestDataAttributesComponentsAffectedItems(
                    id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                    status=PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus.OPERATIONAL,
                ),
            ],
        ),
        type=PatchMaintenanceRequestDataType.MAINTENANCES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_maintenance(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
