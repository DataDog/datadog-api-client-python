"""
Update STS Service Account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_update_request import GCPSTSServiceAccountUpdateRequest
from datadog_api_client.v2.model.gcpsts_service_account_update_request_data import GCPSTSServiceAccountUpdateRequestData

body = GCPSTSServiceAccountUpdateRequest(
    data=GCPSTSServiceAccountUpdateRequestData(
        attributes=GCPSTSServiceAccountAttributes(
            client_email="datadog-service-account@test-project.iam.gserviceaccount.com",
            host_filters=[],
        ),
        id="d291291f-12c2-22g4-j290-123456678897",
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcpsts_account(account_id="account_id", body=body)

    print(response)
