"""
Update a Twilio integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_accounts_api import TwilioIntegrationAccountsApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth
from datadog_api_client.v2.model.twilio_basic_auth_type import TwilioBasicAuthType
from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
from datadog_api_client.v2.model.twilio_dataflow_id import TwilioDataflowId
from datadog_api_client.v2.model.twilio_integration_account_update_attributes import (
    TwilioIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.twilio_integration_account_update_data import TwilioIntegrationAccountUpdateData
from datadog_api_client.v2.model.twilio_integration_account_update_request import TwilioIntegrationAccountUpdateRequest
from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType
from datadog_api_client.v2.model.twilio_interface_update import TwilioInterfaceUpdate
from datadog_api_client.v2.model.twilio_settings_update import TwilioSettingsUpdate

body = TwilioIntegrationAccountUpdateRequest(
    data=TwilioIntegrationAccountUpdateData(
        attributes=TwilioIntegrationAccountUpdateAttributes(
            interface=TwilioInterfaceUpdate(
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
                settings=TwilioSettingsUpdate(
                    account_sid="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    censor_logs=True,
                ),
                type=TwilioInterfaceType.TWILIO,
            ),
            name="twilio-prod",
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_twilio_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationAccountsApi(api_client)
    response = api_instance.update_twilio_integration_account(
        interface_id=TwilioInterfaceType.TWILIO, account_id="account_id", body=body
    )

    print(response)
