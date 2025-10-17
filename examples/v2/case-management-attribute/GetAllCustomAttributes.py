"""
Get all custom attributes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.get_all_custom_attributes()

    print(response)
