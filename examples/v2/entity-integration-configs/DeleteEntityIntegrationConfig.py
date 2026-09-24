"""
Delete an entity integration configuration returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.entity_integration_configs_api import EntityIntegrationConfigsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_entity_integration_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = EntityIntegrationConfigsApi(api_client)
    api_instance.delete_entity_integration_config(
        integration_id="github",
    )
