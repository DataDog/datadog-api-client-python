"""
Update STS Service Account returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.gcpsts_service_account_update_request import GCPSTSServiceAccountUpdateRequestJSON

# there is a valid "gcp_sts_account" in the system
GCP_STS_ACCOUNT_DATA_ID = environ["GCP_STS_ACCOUNT_DATA_ID"]

body = GCPSTSServiceAccountUpdateRequestJSON(
    client_email="252bf553ef04b351@example.com",
    host_filters=[
        "foo:bar",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.update_gcpsts_account(account_id=GCP_STS_ACCOUNT_DATA_ID, body=body)

    print(response)
