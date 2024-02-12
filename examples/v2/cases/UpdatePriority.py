"""
Update case priority returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cases_api import CasesApi
from datadog_api_client.v2.model.case_priority import CasePriority
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_priority import CaseUpdatePriority
from datadog_api_client.v2.model.case_update_priority_attributes import CaseUpdatePriorityAttributes
from datadog_api_client.v2.model.case_update_priority_request import CaseUpdatePriorityRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdatePriorityRequest(
    data=CaseUpdatePriority(
        attributes=CaseUpdatePriorityAttributes(
            priority=CasePriority.P3,
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CasesApi(api_client)
    response = api_instance.update_priority(case_id=CASE_ID, body=body)

    print(response)
