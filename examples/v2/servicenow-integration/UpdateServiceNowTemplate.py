"""
Update ServiceNow template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType
from datadog_api_client.v2.model.service_now_template_update_request import ServiceNowTemplateUpdateRequest
from datadog_api_client.v2.model.service_now_template_update_request_attributes import (
    ServiceNowTemplateUpdateRequestAttributes,
)
from datadog_api_client.v2.model.service_now_template_update_request_data import ServiceNowTemplateUpdateRequestData
from uuid import UUID

body = ServiceNowTemplateUpdateRequest(
    data=ServiceNowTemplateUpdateRequestData(
        attributes=ServiceNowTemplateUpdateRequestAttributes(
            assignment_group_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            business_service_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            fields_mapping=dict(
                category="hardware",
                priority="2",
            ),
            handle_name="incident-template-updated",
            instance_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            servicenow_tablename="incident",
            user_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
        ),
        type=ServiceNowTemplateType.SERVICENOW_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_service_now_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.update_service_now_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
