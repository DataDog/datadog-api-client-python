"""
Update case due date returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_due_date import CaseUpdateDueDate
from datadog_api_client.v2.model.case_update_due_date_attributes import CaseUpdateDueDateAttributes
from datadog_api_client.v2.model.case_update_due_date_request import CaseUpdateDueDateRequest

body = CaseUpdateDueDateRequest(
    data=CaseUpdateDueDate(
        attributes=CaseUpdateDueDateAttributes(
            due_date="2026-12-31",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_case_due_date"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_due_date(case_id="case_id", body=body)

    print(response)
