"""
Update a case view returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType
from datadog_api_client.v2.model.case_view_update import CaseViewUpdate
from datadog_api_client.v2.model.case_view_update_attributes import CaseViewUpdateAttributes
from datadog_api_client.v2.model.case_view_update_request import CaseViewUpdateRequest

body = CaseViewUpdateRequest(
    data=CaseViewUpdate(
        attributes=CaseViewUpdateAttributes(),
        type=CaseViewResourceType.VIEW,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_view(view_id="view_id", body=body)

    print(response)
