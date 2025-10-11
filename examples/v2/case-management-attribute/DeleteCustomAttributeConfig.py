"""
Delete custom attributes config returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

# there is a valid "case_type" in the system
CASE_TYPE_ID = environ["CASE_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ID = environ["CUSTOM_ATTRIBUTE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    api_instance.delete_custom_attribute_config(
        case_type_id=CASE_TYPE_ID,
        custom_attribute_id=CUSTOM_ATTRIBUTE_ID,
    )
