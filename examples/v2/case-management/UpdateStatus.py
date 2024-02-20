"""
Update case status returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_status import CaseStatus
from datadog_api_client.v2.model.case_update_status import CaseUpdateStatus
from datadog_api_client.v2.model.case_update_status_attributes import CaseUpdateStatusAttributes
from datadog_api_client.v2.model.case_update_status_request import CaseUpdateStatusRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateStatusRequest(
    data=CaseUpdateStatus(
        attributes=CaseUpdateStatusAttributes(
            status=CaseStatus.IN_PROGRESS,
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_status(case_id=CASE_ID, body=body)

    print(response)
