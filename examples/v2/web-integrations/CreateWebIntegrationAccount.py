"""
Create a web integration account returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi
from datadog_api_client.v2.model.web_integration_account_create_request import WebIntegrationAccountCreateRequest
from datadog_api_client.v2.model.web_integration_account_create_request_attributes import (
    WebIntegrationAccountCreateRequestAttributes,
)
from datadog_api_client.v2.model.web_integration_account_create_request_data import (
    WebIntegrationAccountCreateRequestData,
)
from datadog_api_client.v2.model.web_integration_account_secrets import WebIntegrationAccountSecrets
from datadog_api_client.v2.model.web_integration_account_settings import WebIntegrationAccountSettings
from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType

body = WebIntegrationAccountCreateRequest(
    data=WebIntegrationAccountCreateRequestData(
        attributes=WebIntegrationAccountCreateRequestAttributes(
            name="my-databricks-account",
            secrets=WebIntegrationAccountSecrets([("client_secret", "my-client-secret")]),
            settings=WebIntegrationAccountSettings([("workspace_url", "https://example.azuredatabricks.net")]),
        ),
        type=WebIntegrationAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_web_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.create_web_integration_account(integration_name="integration_name", body=body)

    print(response)
