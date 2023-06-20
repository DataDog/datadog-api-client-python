"""
Create a new entry for your service account returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcpsts_service_account_create_request import GCPSTSServiceAccountCreateRequestJSON

body = GCPSTSServiceAccountCreateRequestJSON(
    client_email="252bf553ef04b351@test-project.iam.gserviceaccount.com",
    host_filters=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcpsts_account(body=body)

    print(response)
