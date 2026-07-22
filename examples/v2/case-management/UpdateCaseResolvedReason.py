"""
Update case resolved reason returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_resolved_reason import CaseUpdateResolvedReason
from datadog_api_client.v2.model.case_update_resolved_reason_attributes import CaseUpdateResolvedReasonAttributes
from datadog_api_client.v2.model.case_update_resolved_reason_request import CaseUpdateResolvedReasonRequest

body = CaseUpdateResolvedReasonRequest(
    data=CaseUpdateResolvedReason(
        attributes=CaseUpdateResolvedReasonAttributes(
            security_resolved_reason="FALSE_POSITIVE",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_resolved_reason(case_id="case_id", body=body)

    print(response)
