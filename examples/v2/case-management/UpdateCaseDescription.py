"""
Update case description returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_description import CaseUpdateDescription
from datadog_api_client.v2.model.case_update_description_attributes import CaseUpdateDescriptionAttributes
from datadog_api_client.v2.model.case_update_description_request import CaseUpdateDescriptionRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateDescriptionRequest(
    data=CaseUpdateDescription(
        attributes=CaseUpdateDescriptionAttributes(
            description="Seeing some weird memory increase... Updating the description",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_description(case_id=CASE_ID, body=body)

    print(response)
