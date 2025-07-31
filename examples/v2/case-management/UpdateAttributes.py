"""
Update case attributes returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_object_attributes import CaseObjectAttributes
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_attributes import CaseUpdateAttributes
from datadog_api_client.v2.model.case_update_attributes_attributes import CaseUpdateAttributesAttributes
from datadog_api_client.v2.model.case_update_attributes_request import CaseUpdateAttributesRequest

# there is a valid "case" in the system
CASE_ID = environ["CASE_ID"]

body = CaseUpdateAttributesRequest(
    data=CaseUpdateAttributes(
        attributes=CaseUpdateAttributesAttributes(
            attributes=CaseObjectAttributes(
                env=[
                    "test",
                ],
                service=[
                    "web-store",
                    "web-api",
                ],
                team=[
                    "engineer",
                ],
            ),
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_attributes(case_id=CASE_ID, body=body)

    print(response)
