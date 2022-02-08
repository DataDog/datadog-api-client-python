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
    webhook_name = "webhook_name_example"  # str | The name of the webhook.
    body = WebhooksIntegrationUpdateRequest(
        custom_headers="custom_headers_example",
        encode_as=WebhooksIntegrationEncoding("json"),
        name="WEBHOOK_NAME",
        payload="payload_example",
        url="https://example.com/webhook",
    )  # WebhooksIntegrationUpdateRequest | Update an existing Datadog-Webhooks integration.

    # example passing only required values which don't have defaults set
    try:
        # Update a webhook
        api_response = api_instance.update_webhooks_integration(webhook_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhooksIntegrationApi->update_webhooks_integration: %s\n" % e)
