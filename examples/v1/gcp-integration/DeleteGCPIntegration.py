"""
Delete a GCP integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v1.model.gcp_account import GCPAccount

body = GCPAccount(
    client_email="252bf553ef04b351@example.com",
    client_id="163662907116366290710",
    project_id="datadog-apitest",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.delete_gcp_integration(body=body)

    print(response)
