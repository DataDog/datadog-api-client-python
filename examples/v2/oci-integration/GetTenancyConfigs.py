"""
Get tenancy configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
configuration.unstable_operations["get_tenancy_configs"] = True
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    response = api_instance.get_tenancy_configs()

    print(response)
