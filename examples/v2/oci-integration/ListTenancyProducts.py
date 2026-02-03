"""
List tenancy products returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.list_tenancy_products(
        product_keys="productKeys",
    )

    print(response)
