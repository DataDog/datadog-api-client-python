"""
Delete a single kind returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    api_instance.delete_catalog_kind(
        kind_id="my-job",
    )
