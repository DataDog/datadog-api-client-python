"""
List APIs returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.api_management_api import APIManagementApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_apis"] = True
with ApiClient(configuration) as api_client:
    api_instance = APIManagementApi(api_client)
    response = api_instance.list_apis()

    print(response)
