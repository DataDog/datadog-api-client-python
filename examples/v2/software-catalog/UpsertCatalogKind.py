"""
Create or update kinds returns "ACCEPTED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi
from datadog_api_client.v2.model.kind_obj import KindObj

body = KindObj(
    kind="my-job",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.upsert_catalog_kind(body=body)

    print(response)
