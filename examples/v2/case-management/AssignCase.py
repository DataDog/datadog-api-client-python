"""
Assign case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_assign import CaseAssign
from datadog_api_client.v2.model.case_assign_attributes import CaseAssignAttributes
from datadog_api_client.v2.model.case_assign_request import CaseAssignRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = CaseAssignRequest(
    data=CaseAssign(
        attributes=CaseAssignAttributes(
            assignee_id=USER_DATA_ID,
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.assign_case(case_id=CASE_ID, body=body)

    print(response)
