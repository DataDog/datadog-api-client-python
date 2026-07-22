"""
Update a case type returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi
from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType
from datadog_api_client.v2.model.case_type_update import CaseTypeUpdate
from datadog_api_client.v2.model.case_type_update_request import CaseTypeUpdateRequest

body = CaseTypeUpdateRequest(
    data=CaseTypeUpdate(
        attributes=CaseTypeResourceAttributes(
            description="Investigations done in case management",
            emoji="🕵🏻\u200d♂️",
            name="Investigation",
        ),
        type=CaseTypeResourceType.CASE_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    response = api_instance.update_case_type(case_type_id="case_type_id", body=body)

    print(response)
