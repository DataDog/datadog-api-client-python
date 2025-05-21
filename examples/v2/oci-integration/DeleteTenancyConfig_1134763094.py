"""
Delete tenancy config for non-existing tenancy returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    api_instance.delete_tenancy_config(
        tenancy_ocid="ocid1.tenancy.fake",
    )
