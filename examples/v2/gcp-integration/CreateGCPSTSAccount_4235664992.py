"""
Create a new entry for your service account with cspm enabled returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_create_request import GCPSTSServiceAccountCreateRequest
from datadog_api_client.v2.model.gcpsts_service_account_data import GCPSTSServiceAccountData

body = GCPSTSServiceAccountCreateRequest(
    data=GCPSTSServiceAccountData(
        attributes=GCPSTSServiceAccountAttributes(
            is_cspm_enabled=True,
            resource_collection_enabled=True,
            client_email="252bf553ef04b351@test-project.iam.gserviceaccount.com",
            host_filters=[],
        ),
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcpsts_account(body=body)

    print(response)
