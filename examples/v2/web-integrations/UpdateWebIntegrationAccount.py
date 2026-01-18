"""
Update integration account returns "OK" response
"""

from os import environ
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

# there is a valid "web_integration_account" in the system
WEB_INTEGRATION_ACCOUNT_DATA_ID = environ["WEB_INTEGRATION_ACCOUNT_DATA_ID"]

body = WebIntegrationAccountUpdateRequest(
    data=WebIntegrationAccountUpdateRequestData(
        type=WebIntegrationAccountType.ACCOUNT,
        attributes=WebIntegrationAccountUpdateRequestAttributes(
            name="Example-Web-Integration-updated",
            settings=dict([("events", "False"), ("messages", "False"), ("ccm_enabled", "False")]),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.update_web_integration_account(
        integration_name="twilio", account_id=WEB_INTEGRATION_ACCOUNT_DATA_ID, body=body
    )

    print(response)
