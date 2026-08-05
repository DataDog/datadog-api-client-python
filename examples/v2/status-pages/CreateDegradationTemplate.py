"""
Create degradation template returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
    CreateDegradationRequestDataAttributesStatus,
)
from datadog_api_client.v2.model.create_degradation_template_request import CreateDegradationTemplateRequest
from datadog_api_client.v2.model.create_degradation_template_request_data import CreateDegradationTemplateRequestData
from datadog_api_client.v2.model.create_degradation_template_request_data_attributes import (
    CreateDegradationTemplateRequestDataAttributes,
)
from datadog_api_client.v2.model.create_degradation_template_request_data_attributes_components_affected_items import (
    CreateDegradationTemplateRequestDataAttributesComponentsAffectedItems,
)
from datadog_api_client.v2.model.create_degradation_template_request_data_attributes_updates_items import (
    CreateDegradationTemplateRequestDataAttributesUpdatesItems,
)
from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_components_affected_items_status import (
    PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus,
)
from datadog_api_client.v2.model.patch_degradation_template_request_data_type import (
    PatchDegradationTemplateRequestDataType,
)
from uuid import UUID

body = CreateDegradationTemplateRequest(
    data=CreateDegradationTemplateRequestData(
        attributes=CreateDegradationTemplateRequestDataAttributes(
            components_affected=[
                CreateDegradationTemplateRequestDataAttributesComponentsAffectedItems(
                    id="",
                    status=PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus.OPERATIONAL,
                ),
            ],
            name="",
            updates=[
                CreateDegradationTemplateRequestDataAttributesUpdatesItems(
                    status=CreateDegradationRequestDataAttributesStatus.INVESTIGATING,
                ),
            ],
        ),
        type=PatchDegradationTemplateRequestDataType.DEGRADATION_TEMPLATES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_degradation_template(page_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
