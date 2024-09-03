"""
Delete a single entity returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    api_instance.delete_catalog_entity(
        entity_id="service:myservice",
    )
