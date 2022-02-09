import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import azure_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = azure_integration_api.AzureIntegrationApi(api_client)
    body = AzureAccount(
        automute=True,
        client_id="testc7f6-1234-5678-9101-3fcbf464test",
        client_secret="testingx./Sw*g/Y33t..R1cH+hScMDt",
        errors=["*"],
        host_filters="key:value,filter:example",
        new_client_id="new1c7f6-1234-5678-9101-3fcbf464test",
        new_tenant_name="new1c44-1234-5678-9101-cc00736ftest",
        tenant_name="testc44-1234-5678-9101-cc00736ftest",
    )  # AzureAccount | Update a Datadog-Azure integration's host filters request body.

    # example passing only required values which don't have defaults set
    try:
        # Update Azure integration host filters
        api_response = api_instance.update_azure_host_filters(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AzureIntegrationApi->update_azure_host_filters: %s\n" % e)
