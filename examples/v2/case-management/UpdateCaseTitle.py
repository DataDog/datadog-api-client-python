"""
Update case title returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_title import CaseUpdateTitle
from datadog_api_client.v2.model.case_update_title_attributes import CaseUpdateTitleAttributes
from datadog_api_client.v2.model.case_update_title_request import CaseUpdateTitleRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateTitleRequest(
    data=CaseUpdateTitle(
        attributes=CaseUpdateTitleAttributes(
            title="[UPDATED] Memory leak investigation on API",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_title(case_id=CASE_ID, body=body)

    print(response)
