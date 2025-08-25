"""
Delete custom attribute from case returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

# there is a valid "case" with a custom "case_type" in the system
CASE_WITH_TYPE_ID = environ["CASE_WITH_TYPE_ID"]

# there is a valid "custom_attribute" in the system
CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY = environ["CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.delete_case_custom_attribute(
        case_id=CASE_WITH_TYPE_ID,
        custom_attribute_key=CUSTOM_ATTRIBUTE_ATTRIBUTES_KEY,
    )

    print(response)
