"""
Delete tenancy config returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.oci_integration_api import OCIIntegrationApi

# there is a valid "oci_tenancy" resource in the system
OCI_TENANCY_DATA_ID = environ["OCI_TENANCY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OCIIntegrationApi(api_client)
    api_instance.delete_tenancy_config(
        tenancy_ocid=OCI_TENANCY_DATA_ID,
    )
