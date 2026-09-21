"""
Get a list of entity relations returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    items = api_instance.list_catalog_relation_with_pagination(
        page_limit=20,
    )
    for item in items:
        print(item)
