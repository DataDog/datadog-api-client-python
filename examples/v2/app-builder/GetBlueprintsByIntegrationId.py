"""
Get Blueprints by Integration ID returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.get_blueprints_by_integration_id(
        integration_id="aws",
    )

    print(response)
