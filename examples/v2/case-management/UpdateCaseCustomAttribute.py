"""
Update case custom attribute returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_custom_attribute import CaseUpdateCustomAttribute
from datadog_api_client.v2.model.case_update_custom_attribute_request import CaseUpdateCustomAttributeRequest
from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType
from datadog_api_client.v2.model.custom_attribute_value import CustomAttributeValue

# there is a valid "case" with a custom "case_type" in the system
CASE_WITH_TYPE_ID = environ["CASE_WITH_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = environ["CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY"]

body = CaseUpdateCustomAttributeRequest(
    data=CaseUpdateCustomAttribute(
        attributes=CustomAttributeValue(
            type=CustomAttributeType.TEXT,
            is_multi=True,
            value=["Abba", "The Cure"],
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_custom_attribute(
        case_id=CASE_WITH_TYPE_ID, custom_attribute_key=CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY, body=body
    )

    print(response)
