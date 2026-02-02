"""
Decline recommended entities in bulk returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi
from datadog_api_client.v2.model.recommended_entity_id import RecommendedEntityID

body = [
    RecommendedEntityID(
        id="123abcdef",
    ),
]

configuration = Configuration()
configuration.unstable_operations["decline_recommended_entities"] = True
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    api_instance.decline_recommended_entities(body=body)
