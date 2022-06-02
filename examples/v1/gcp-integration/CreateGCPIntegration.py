"""
Create a GCP integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi
from datadog_api_client.v1.model.gcp_account import GCPAccount

body = GCPAccount(
    auth_provider_x509_cert_url="https://www.googleapis.com/oauth2/v1/certs",
    auth_uri="https://accounts.google.com/o/oauth2/auth",
    client_email="api-dev@datadog-sandbox.iam.gserviceaccount.com",
    client_id="123456712345671234567",
    client_x509_cert_url="https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL",
    errors=[
        "*",
    ],
    host_filters="key:value,filter:example",
    private_key="private_key",
    private_key_id="123456789abcdefghi123456789abcdefghijklm",
    project_id="datadog-apitest",
    token_uri="https://accounts.google.com/o/oauth2/token",
    type="service_account",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GCPIntegrationApi(api_client)
    response = api_instance.create_gcp_integration(body=body)

    print(response)
