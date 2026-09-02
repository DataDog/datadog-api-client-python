"""
List SKUs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_catalog_api import ProductCatalogApi
from datadog_api_client.v2.model.product_catalog_sk_us_api_version import ProductCatalogSKUsAPIVersion

configuration = Configuration()
configuration.unstable_operations["list_product_catalog_sk_us"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductCatalogApi(api_client)
    response = api_instance.list_product_catalog_sk_us(
        version=ProductCatalogSKUsAPIVersion.V1,
    )

    print(response)
