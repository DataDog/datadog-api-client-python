import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import gcp_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gcp_integration_api.GCPIntegrationApi(api_client)
    body = GCPAccount(
        auth_provider_x509_cert_url="https://www.googleapis.com/oauth2/v1/certs",
        auth_uri="https://accounts.google.com/o/oauth2/auth",
        automute=True,
        client_email="api-dev@datadog-sandbox.iam.gserviceaccount.com",
        client_id="123456712345671234567",
        client_x509_cert_url="https://www.googleapis.com/robot/v1/metadata/x509/<CLIENT_EMAIL>",
        errors=["*"],
        host_filters="key:value,filter:example",
        private_key="private_key",
        private_key_id="123456789abcdefghi123456789abcdefghijklm",
        project_id="datadog-apitest",
        token_uri="https://accounts.google.com/o/oauth2/token",
        type="service_account",
    )  # GCPAccount | Create a Datadog-GCP integration.

    # example passing only required values which don't have defaults set
    try:
        # Create a GCP integration
        api_response = api_instance.create_gcp_integration(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GCPIntegrationApi->create_gcp_integration: %s\n" % e)
