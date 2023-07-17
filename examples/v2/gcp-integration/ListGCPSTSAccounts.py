"""
List all GCP STS-enabled service accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.list_gcpsts_accounts()

    print(response)
