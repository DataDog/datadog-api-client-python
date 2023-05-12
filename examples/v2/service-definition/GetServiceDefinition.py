"""
Get a single service definition returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_schema_versions import ServiceDefinitionSchemaVersions

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.get_service_definition(
        service_name="service-definition-test",
        schema_version=ServiceDefinitionSchemaVersions.V2_1,
    )

    print(response)
