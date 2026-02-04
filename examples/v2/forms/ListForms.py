"""
List all forms returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi

configuration = Configuration()
configuration.unstable_operations["list_forms"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.list_forms()

    print(response)
