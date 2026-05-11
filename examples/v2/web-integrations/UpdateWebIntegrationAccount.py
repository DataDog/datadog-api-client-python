"""
Update a web integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi
from datadog_api_client.v2.model.web_integration_account_secrets import WebIntegrationAccountSecrets
from datadog_api_client.v2.model.web_integration_account_settings import WebIntegrationAccountSettings
from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType
from datadog_api_client.v2.model.web_integration_account_update_request import WebIntegrationAccountUpdateRequest
from datadog_api_client.v2.model.web_integration_account_update_request_attributes import (
    WebIntegrationAccountUpdateRequestAttributes,
)
from datadog_api_client.v2.model.web_integration_account_update_request_data import (
    WebIntegrationAccountUpdateRequestData,
)

body = WebIntegrationAccountUpdateRequest(
    data=WebIntegrationAccountUpdateRequestData(
        attributes=WebIntegrationAccountUpdateRequestAttributes(
            name="my-databricks-account",
            secrets=WebIntegrationAccountSecrets([("client_secret", "my-client-secret")]),
            settings=WebIntegrationAccountSettings([("workspace_url", "https://example.azuredatabricks.net")]),
        ),
        type=WebIntegrationAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_web_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.update_web_integration_account(
        integration_name="integration_name", account_id="account_id", body=body
    )

    print(response)
