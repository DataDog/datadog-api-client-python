"""
Create a Twilio integration account returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_accounts_api import TwilioIntegrationAccountsApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.twilio_account_attributes import TwilioAccountAttributes
from datadog_api_client.v2.model.twilio_account_create_data import TwilioAccountCreateData
from datadog_api_client.v2.model.twilio_account_request import TwilioAccountRequest
from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth
from datadog_api_client.v2.model.twilio_basic_auth_type import TwilioBasicAuthType
from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
from datadog_api_client.v2.model.twilio_dataflow_id import TwilioDataflowId
from datadog_api_client.v2.model.twilio_settings import TwilioSettings

body = TwilioAccountRequest(
    data=TwilioAccountCreateData(
        attributes=TwilioAccountAttributes(
            authentication=TwilioBasicAuth(
                api_key="SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                api_key_token="your-api-key-secret",
                type=TwilioBasicAuthType.BASIC,
            ),
            dataflows=[
                TwilioDataflow(
                    enabled=True,
                    id=TwilioDataflowId.MESSAGES_LOGS,
                ),
            ],
            name="twilio-prod",
            settings=TwilioSettings(
                account_sid="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                censor_logs=True,
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_twilio_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationAccountsApi(api_client)
    response = api_instance.create_twilio_account(body=body)

    print(response)
