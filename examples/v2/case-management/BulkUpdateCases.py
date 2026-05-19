"""
Bulk update cases returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_bulk_action_type import CaseBulkActionType
from datadog_api_client.v2.model.case_bulk_resource_type import CaseBulkResourceType
from datadog_api_client.v2.model.case_bulk_update_request import CaseBulkUpdateRequest
from datadog_api_client.v2.model.case_bulk_update_request_attributes import CaseBulkUpdateRequestAttributes
from datadog_api_client.v2.model.case_bulk_update_request_data import CaseBulkUpdateRequestData

body = CaseBulkUpdateRequest(
    data=CaseBulkUpdateRequestData(
        attributes=CaseBulkUpdateRequestAttributes(
            case_ids=[
                "case-id-1",
                "case-id-2",
            ],
            payload=dict(
                priority="P1",
            ),
            type=CaseBulkActionType.PRIORITY,
        ),
        type=CaseBulkResourceType.BULK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["bulk_update_cases"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.bulk_update_cases(body=body)
