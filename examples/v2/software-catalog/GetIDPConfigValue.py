"""
Get Internal Developer Portal configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi

configuration = Configuration()
configuration.unstable_operations["get_idp_config_value"] = True
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.get_idp_config_value(
        config_name="idp_pinned_dashboards",
    )

    print(response)
