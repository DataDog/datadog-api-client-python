"""
List AI workflows returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dependency_management_api import DependencyManagementApi

configuration = Configuration()
configuration.unstable_operations["list_ai_workflows"] = True
with ApiClient(configuration) as api_client:
    api_instance = DependencyManagementApi(api_client)
    response = api_instance.list_ai_workflows()

    print(response)
