"""
Create integration account returns "Created: The account was successfully created." response
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
from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType

body = WebIntegrationAccountCreateRequest(
    data=WebIntegrationAccountCreateRequestData(
        attributes=WebIntegrationAccountCreateRequestAttributes(
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
        type=WebIntegrationAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.create_web_integration_account(integration_name="integration_name", body=body)

    print(response)
