"""
Create an integration account returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi
from datadog_api_client.v2.model.integration_account_attributes import IntegrationAccountAttributes
from datadog_api_client.v2.model.integration_account_create_data import IntegrationAccountCreateData
from datadog_api_client.v2.model.integration_account_integration_id import IntegrationAccountIntegrationId
from datadog_api_client.v2.model.integration_account_interface_id import IntegrationAccountInterfaceId
from datadog_api_client.v2.model.integration_account_request import IntegrationAccountRequest
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth
from datadog_api_client.v2.model.twilio_basic_auth_type import TwilioBasicAuthType
from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
from datadog_api_client.v2.model.twilio_dataflow_id import TwilioDataflowId
from datadog_api_client.v2.model.twilio_integration import TwilioIntegration
from datadog_api_client.v2.model.twilio_integration_type import TwilioIntegrationType
from datadog_api_client.v2.model.twilio_interface import TwilioInterface
from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType
from datadog_api_client.v2.model.twilio_settings import TwilioSettings

body = IntegrationAccountRequest(
    data=IntegrationAccountCreateData(
        attributes=IntegrationAccountAttributes(
            integration=TwilioIntegration(
                interface=TwilioInterface(
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
                    settings=TwilioSettings(
                        account_sid="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        censor_logs=True,
                    ),
                    type=TwilioInterfaceType.TWILIO,
                ),
                type=TwilioIntegrationType.TWILIO,
            ),
            name="twilio-prod",
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    response = api_instance.create_integration_account(
        integration_id=IntegrationAccountIntegrationId.TWILIO,
        interface_id=IntegrationAccountInterfaceId.TWILIO,
        body=body,
    )

    print(response)
