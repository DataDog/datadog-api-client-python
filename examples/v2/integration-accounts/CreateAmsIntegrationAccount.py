"""
Create integration account returns "Created: The account was successfully created." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi
from datadog_api_client.v2.model.ams_integration_account_create_request import AmsIntegrationAccountCreateRequest
from datadog_api_client.v2.model.ams_integration_account_create_request_attributes import (
    AmsIntegrationAccountCreateRequestAttributes,
)
from datadog_api_client.v2.model.ams_integration_account_create_request_data import (
    AmsIntegrationAccountCreateRequestData,
)
from datadog_api_client.v2.model.ams_integration_account_type import AmsIntegrationAccountType

body = AmsIntegrationAccountCreateRequest(
    data=AmsIntegrationAccountCreateRequestData(
        attributes=AmsIntegrationAccountCreateRequestAttributes(
            name="My Production Account",
            secrets=dict([("api_key_token", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")]),
            settings=dict(
                [
                    ("account_sid", "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
                    ("alerts", "True"),
                    ("api_key", "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
                    ("call_summaries", "True"),
                    ("ccm_enabled", "True"),
                    ("censor_logs", "True"),
                    ("events", "True"),
                    ("messages", "True"),
                ]
            ),
        ),
        type=AmsIntegrationAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    response = api_instance.create_ams_integration_account(
        integration_name="integration_name", interface_id="interface_id", body=body
    )

    print(response)
