"""
Update a custom variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration_custom_variable_update_request import (
    WebhooksIntegrationCustomVariableUpdateRequest,
)

# there is a valid "webhook_custom_variable" in the system
WEBHOOK_CUSTOM_VARIABLE_NAME = environ["WEBHOOK_CUSTOM_VARIABLE_NAME"]

body = WebhooksIntegrationCustomVariableUpdateRequest(
    value="variable-updated",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.update_webhooks_integration_custom_variable(
        custom_variable_name=WEBHOOK_CUSTOM_VARIABLE_NAME, body=body
    )

    print(response)
