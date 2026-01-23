"""
Create ServiceNow template returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from datadog_api_client.v2.model.service_now_template_create_request import ServiceNowTemplateCreateRequest
from datadog_api_client.v2.model.service_now_template_create_request_attributes import (
    ServiceNowTemplateCreateRequestAttributes,
)
from datadog_api_client.v2.model.service_now_template_create_request_data import ServiceNowTemplateCreateRequestData
from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType
from uuid import UUID

body = ServiceNowTemplateCreateRequest(
    data=ServiceNowTemplateCreateRequestData(
        attributes=ServiceNowTemplateCreateRequestAttributes(
            assignment_group_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            business_service_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            fields_mapping=dict(
                category="software",
                priority="1",
            ),
            handle_name="incident-template",
            instance_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
            servicenow_tablename="incident",
            user_id=UUID("65b3341b-0680-47f9-a6d4-134db45c603e"),
        ),
        type=ServiceNowTemplateType.SERVICENOW_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_service_now_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.create_service_now_template(body=body)

    print(response)
