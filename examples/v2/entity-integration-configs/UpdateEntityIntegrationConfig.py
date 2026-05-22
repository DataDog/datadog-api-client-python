"""
Create or update entity integration configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.entity_integration_configs_api import EntityIntegrationConfigsApi
from datadog_api_client.v2.model.entity_integration_config_payload import EntityIntegrationConfigPayload
from datadog_api_client.v2.model.entity_integration_config_request import EntityIntegrationConfigRequest
from datadog_api_client.v2.model.entity_integration_config_request_attributes import (
    EntityIntegrationConfigRequestAttributes,
)
from datadog_api_client.v2.model.entity_integration_config_request_data import EntityIntegrationConfigRequestData
from datadog_api_client.v2.model.entity_integration_config_request_type import EntityIntegrationConfigRequestType

body = EntityIntegrationConfigRequest(
    data=EntityIntegrationConfigRequestData(
        attributes=EntityIntegrationConfigRequestAttributes(
            config=EntityIntegrationConfigPayload(
                [("enabled_repos", "[{'github_org_name': 'myorg', 'hostname': 'github.com', 'repo_name': 'myrepo'}]")]
            ),
        ),
        type=EntityIntegrationConfigRequestType.ENTITY_INTEGRATION_CONFIG_REQUESTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_entity_integration_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = EntityIntegrationConfigsApi(api_client)
    response = api_instance.update_entity_integration_config(integration_id="github", body=body)

    print(response)
