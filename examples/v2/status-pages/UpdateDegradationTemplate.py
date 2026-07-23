"""
Update degradation template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
    CreateDegradationRequestDataAttributesStatus,
)
from datadog_api_client.v2.model.patch_degradation_template_request import PatchDegradationTemplateRequest
from datadog_api_client.v2.model.patch_degradation_template_request_data import PatchDegradationTemplateRequestData
from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes import (
    PatchDegradationTemplateRequestDataAttributes,
)
from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_components_affected_items import (
    PatchDegradationTemplateRequestDataAttributesComponentsAffectedItems,
)
from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_components_affected_items_status import (
    PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus,
)
from datadog_api_client.v2.model.patch_degradation_template_request_data_attributes_updates_items import (
    PatchDegradationTemplateRequestDataAttributesUpdatesItems,
)
from datadog_api_client.v2.model.patch_degradation_template_request_data_type import (
    PatchDegradationTemplateRequestDataType,
)
from uuid import UUID

body = PatchDegradationTemplateRequest(
    data=PatchDegradationTemplateRequestData(
        attributes=PatchDegradationTemplateRequestDataAttributes(
            components_affected=[
                PatchDegradationTemplateRequestDataAttributesComponentsAffectedItems(
                    id="",
                    status=PatchDegradationTemplateRequestDataAttributesComponentsAffectedItemsStatus.OPERATIONAL,
                ),
            ],
            updates=[
                PatchDegradationTemplateRequestDataAttributesUpdatesItems(
                    status=CreateDegradationRequestDataAttributesStatus.INVESTIGATING,
                ),
            ],
        ),
        id="",
        type=PatchDegradationTemplateRequestDataType.DEGRADATION_TEMPLATES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_degradation_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        page_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        body=body,
    )

    print(response)
