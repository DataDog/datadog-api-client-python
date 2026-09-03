"""
Update integration account returns "OK: The account was successfully updated." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi
from datadog_api_client.v2.model.ams_integration_account_type import AmsIntegrationAccountType
from datadog_api_client.v2.model.ams_integration_account_update_request import AmsIntegrationAccountUpdateRequest
from datadog_api_client.v2.model.ams_integration_account_update_request_attributes import (
    AmsIntegrationAccountUpdateRequestAttributes,
)
from datadog_api_client.v2.model.ams_integration_account_update_request_data import (
    AmsIntegrationAccountUpdateRequestData,
)

body = AmsIntegrationAccountUpdateRequest(
    data=AmsIntegrationAccountUpdateRequestData(
        attributes=AmsIntegrationAccountUpdateRequestAttributes(
            name="My Production Account (Updated)",
            secrets=dict([("api_key_token", "new_secret_token_value")]),
            settings=dict([("ccm_enabled", "True"), ("events", "True"), ("messages", "False")]),
        ),
        type=AmsIntegrationAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    response = api_instance.update_ams_integration_account(
        integration_name="integration_name", interface_id="interface_id", account_id="account_id", body=body
    )

    print(response)
