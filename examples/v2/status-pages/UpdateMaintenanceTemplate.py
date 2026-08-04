"""
Update maintenance template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_maintenance_template_request import PatchMaintenanceTemplateRequest
from datadog_api_client.v2.model.patch_maintenance_template_request_data import PatchMaintenanceTemplateRequestData
from datadog_api_client.v2.model.patch_maintenance_template_request_data_attributes import (
    PatchMaintenanceTemplateRequestDataAttributes,
)
from datadog_api_client.v2.model.patch_maintenance_template_request_data_type import (
    PatchMaintenanceTemplateRequestDataType,
)
from uuid import UUID

body = PatchMaintenanceTemplateRequest(
    data=PatchMaintenanceTemplateRequestData(
        attributes=PatchMaintenanceTemplateRequestDataAttributes(
            component_ids=[],
        ),
        id="",
        type=PatchMaintenanceTemplateRequestDataType.MAINTENANCE_TEMPLATES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_maintenance_template(
        page_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
        body=body,
    )

    print(response)
