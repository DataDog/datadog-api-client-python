"""
List role templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

configuration = Configuration()
configuration.unstable_operations["list_role_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.list_role_templates()

    print(response)
