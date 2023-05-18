"""
Create a new entry for your service account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v2.model.attribute_metadata import AttributeMetadata
from datadog_api_client.v2.model.service_account_metadata import ServiceAccountMetadata
from datadog_api_client.v2.model.service_account_to_be_created_data import ServiceAccountToBeCreatedData

body = ServiceAccountToBeCreatedData(
    data=ServiceAccountMetadata(
        attributes=AttributeMetadata(
            client_email="dd-integration@datadog-staging.iam.gserviceaccount.com",
            host_filters=[],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcpsts_accounts_v2(body=body)

    print(response)
