"""
Create degradation returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_degradation_request import CreateDegradationRequest
from datadog_api_client.v2.model.create_degradation_request_data import CreateDegradationRequestData
from datadog_api_client.v2.model.create_degradation_request_data_attributes import (
    CreateDegradationRequestDataAttributes,
)
from datadog_api_client.v2.model.create_degradation_request_data_attributes_components_affected_items import (
    CreateDegradationRequestDataAttributesComponentsAffectedItems,
)
from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
    CreateDegradationRequestDataAttributesStatus,
)
from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType
from datadog_api_client.v2.model.status_pages_component_data_attributes_status import (
    StatusPagesComponentDataAttributesStatus,
)

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = environ[
    "STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"
]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = CreateDegradationRequest(
    data=CreateDegradationRequestData(
        attributes=CreateDegradationRequestDataAttributes(
            components_affected=[
                CreateDegradationRequestDataAttributesComponentsAffectedItems(
                    id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                    status=StatusPagesComponentDataAttributesStatus.MAJOR_OUTAGE,
                ),
            ],
            description="Our API is experiencing elevated latency. We are investigating the issue.",
            status=CreateDegradationRequestDataAttributesStatus.INVESTIGATING,
            title="Elevated API Latency",
        ),
        type=PatchDegradationRequestDataType.DEGRADATIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_degradation(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
