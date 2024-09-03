"""
Get a list of entities returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    items = api_instance.list_catalog_entity_with_pagination()
    for item in items:
        print(item)
