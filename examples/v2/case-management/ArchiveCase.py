"""
Archive case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_empty import CaseEmpty
from datadog_api_client.v2.model.case_empty_request import CaseEmptyRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseEmptyRequest(
    data=CaseEmpty(
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.archive_case(case_id=CASE_ID, body=body)

    print(response)
