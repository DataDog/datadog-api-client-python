"""
Get all service definitions returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    items = api_instance.list_service_definitions_with_pagination(
        page_size=2,
    )
    for item in items:
        print(item)
