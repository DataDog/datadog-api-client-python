"""
Delete tenancy config returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    api_instance.delete_tenancy_config(
        tenancy_ocid="tenancy_ocid",
    )
