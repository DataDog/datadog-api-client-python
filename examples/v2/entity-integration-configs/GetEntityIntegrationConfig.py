"""
Get an entity integration configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.entity_integration_configs_api import EntityIntegrationConfigsApi

configuration = Configuration()
configuration.unstable_operations["get_entity_integration_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = EntityIntegrationConfigsApi(api_client)
    response = api_instance.get_entity_integration_config(
        integration_id="github",
    )

    print(response)
