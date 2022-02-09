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
    body = WebhooksIntegration(
        custom_headers="custom_headers_example",
        encode_as=WebhooksIntegrationEncoding("json"),
        name="WEBHOOK_NAME",
        payload="payload_example",
        url="https://example.com/webhook",
    )  # WebhooksIntegration | Create a webhooks integration request body.

    # example passing only required values which don't have defaults set
    try:
        # Create a webhooks integration
        api_response = api_instance.create_webhooks_integration(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->create_webhooks_integration: %s\n" % e)
