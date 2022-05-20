"""
Create a custom variable returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.webhooks_integration_api import WebhooksIntegrationApi
from datadog_api_client.v1.model.webhooks_integration_custom_variable import WebhooksIntegrationCustomVariable

body = WebhooksIntegrationCustomVariable(
    is_secret=True,
    name="EXAMPLECREATEACUSTOMVARIABLERETURNSOKRESPONSE",
    value="CUSTOM_VARIABLE_VALUE",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebhooksIntegrationApi(api_client)
    response = api_instance.create_webhooks_integration_custom_variable(body=body)

    print(response)
