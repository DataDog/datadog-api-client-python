"""
Get user's project favorites returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
configuration.unstable_operations["list_user_project_favorites"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.list_user_project_favorites()

    print(response)
