"""
Update STS Service Account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcp_service_account_type import GCPServiceAccountType
from datadog_api_client.v2.model.gcpsts_service_account_attributes import GCPSTSServiceAccountAttributes
from datadog_api_client.v2.model.gcpsts_service_account_update_request import GCPSTSServiceAccountUpdateRequest
from datadog_api_client.v2.model.gcpsts_service_account_update_request_data import GCPSTSServiceAccountUpdateRequestData

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = environ["GCP_STS_ACCOUNT_DATA_ID"]

body = GCPSTSServiceAccountUpdateRequest(
    data=GCPSTSServiceAccountUpdateRequestData(
        attributes=GCPSTSServiceAccountAttributes(
            client_email="252bf553ef04b351@example.com",
            host_filters=[
                "foo:bar",
            ],
        ),
        id=GCP_STS_ACCOUNT_DATA_ID,
        type=GCPServiceAccountType.GCP_SERVICE_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcpsts_account(account_id=GCP_STS_ACCOUNT_DATA_ID, body=body)

    print(response)
