"""
Create custom attribute config for a case type returns "CREATED" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi
from datadog_api_client.v2.model.custom_attribute_config_attributes_create import CustomAttributeConfigAttributesCreate
from datadog_api_client.v2.model.custom_attribute_config_create import CustomAttributeConfigCreate
from datadog_api_client.v2.model.custom_attribute_config_create_request import CustomAttributeConfigCreateRequest
from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType
from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

body = CustomAttributeConfigCreateRequest(
    data=CustomAttributeConfigCreate(
        attributes=CustomAttributeConfigAttributesCreate(
            display_name="AWS Region 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
            is_multi=True,
            key="region_d9fe56bc9274fbb6",
            type=CustomAttributeType.NUMBER,
        ),
        type=CustomAttributeConfigResourceType.CUSTOM_ATTRIBUTE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.create_custom_attribute_config(case_type_id=CASE_TYPE_ID, body=body)

    print(response)
