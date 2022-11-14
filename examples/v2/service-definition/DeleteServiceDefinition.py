"""
Delete a single service definition returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    api_instance.delete_service_definition(
        service_name="service-definition-test",
    )
