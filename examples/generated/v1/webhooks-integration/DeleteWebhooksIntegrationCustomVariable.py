import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import webhooks_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_integration_api.WebhooksIntegrationApi(api_client)
    custom_variable_name = "custom_variable_name_example"  # str | The name of the custom variable.

    # example passing only required values which don't have defaults set
    try:
        # Delete a custom variable
        api_instance.delete_webhooks_integration_custom_variable(custom_variable_name)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->delete_webhooks_integration_custom_variable: %s\n" % e)
