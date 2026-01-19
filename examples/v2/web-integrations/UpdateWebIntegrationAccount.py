"""
Update integration account returns "OK: The account was successfully updated." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi
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
            name="My Production Account (Updated)",
            secrets=dict([("api_key_token", "new_secret_token_value")]),
            settings=dict([("ccm_enabled", "True"), ("events", "True"), ("messages", "False")]),
        ),
        type=WebIntegrationAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.update_web_integration_account(
        integration_name="integration_name", account_id="account_id", body=body
    )

    print(response)
