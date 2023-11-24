"""
Delete an STS enabled GCP Account returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = environ["GCP_STS_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    api_instance.delete_gcpsts_account(
        account_id=GCP_STS_ACCOUNT_DATA_ID,
    )
