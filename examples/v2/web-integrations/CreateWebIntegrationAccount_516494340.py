"""
Create integration account returns "Created" response
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
        type=WebIntegrationAccountType.ACCOUNT,
        attributes=WebIntegrationAccountCreateRequestAttributes(
            name="Example-Web-Integration",
            settings=dict(
                [
                    ("api_key", "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
                    ("account_sid", "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
                    ("events", "True"),
                    ("messages", "True"),
                    ("alerts", "True"),
                    ("call_summaries", "True"),
                    ("ccm_enabled", "True"),
                    ("censor_logs", "True"),
                ]
            ),
            secrets=dict([("api_key_token", "test_secret_token")]),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.create_web_integration_account(integration_name="twilio", body=body)

    print(response)
