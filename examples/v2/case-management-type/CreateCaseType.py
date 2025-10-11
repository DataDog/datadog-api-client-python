"""
Create a case type returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi
from datadog_api_client.v2.model.case_type_create import CaseTypeCreate
from datadog_api_client.v2.model.case_type_create_request import CaseTypeCreateRequest
from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType

body = CaseTypeCreateRequest(
    data=CaseTypeCreate(
        attributes=CaseTypeResourceAttributes(
            description="Investigations done in case management",
            emoji="👑",
            name="Investigation",
        ),
        type=CaseTypeResourceType.CASE_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    response = api_instance.create_case_type(body=body)

    print(response)
