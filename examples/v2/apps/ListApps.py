"""
List Apps returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apps_api import AppsApi

configuration = Configuration()
configuration.unstable_operations["list_apps"] = True
with ApiClient(configuration) as api_client:
    api_instance = AppsApi(api_client)
    response = api_instance.list_apps()

    print(response)
