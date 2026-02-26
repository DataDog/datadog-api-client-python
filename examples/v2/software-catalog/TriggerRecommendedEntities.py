"""
Trigger recommended entity discovery returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
configuration.unstable_operations["trigger_recommended_entities"] = True
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.trigger_recommended_entities()

    print(response)
