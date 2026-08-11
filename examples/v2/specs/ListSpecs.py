"""
List API specs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.specs_api import SpecsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpecsApi(api_client)
    response = api_instance.list_specs()

    print(response)
