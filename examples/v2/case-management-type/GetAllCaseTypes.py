"""
Get all case types returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_type_api import CaseManagementTypeApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementTypeApi(api_client)
    response = api_instance.get_all_case_types()

    print(response)
