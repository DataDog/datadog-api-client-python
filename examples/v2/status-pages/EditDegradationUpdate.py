"""
Edit degradation update returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_degradation_update_request import PatchDegradationUpdateRequest
from datadog_api_client.v2.model.patch_degradation_update_request_data import PatchDegradationUpdateRequestData
from datadog_api_client.v2.model.patch_degradation_update_request_data_attributes import (
    PatchDegradationUpdateRequestDataAttributes,
)
from datadog_api_client.v2.model.patch_degradation_update_request_data_attributes_status import (
    PatchDegradationUpdateRequestDataAttributesStatus,
)
from datadog_api_client.v2.model.patch_degradation_update_request_data_type import PatchDegradationUpdateRequestDataType
from uuid import UUID

body = PatchDegradationUpdateRequest(
    data=PatchDegradationUpdateRequestData(
        attributes=PatchDegradationUpdateRequestDataAttributes(
            description="We've identified the source of the latency increase and are deploying a fix.",
            status=PatchDegradationUpdateRequestDataAttributesStatus.IDENTIFIED,
        ),
        id="00000000-0000-0000-0000-000000000000",
        type=PatchDegradationUpdateRequestDataType.DEGRADATION_UPDATES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.edit_degradation_update(
        degradation_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        page_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        update_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        body=body,
    )

    print(response)
