"""
Update an integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.integration_accounts_api import IntegrationAccountsApi
from datadog_api_client.v2.model.integration_account_integration_id import IntegrationAccountIntegrationId
from datadog_api_client.v2.model.integration_account_interface_id import IntegrationAccountInterfaceId
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.integration_account_update_attributes import IntegrationAccountUpdateAttributes
from datadog_api_client.v2.model.integration_account_update_data import IntegrationAccountUpdateData
from datadog_api_client.v2.model.integration_account_update_request import IntegrationAccountUpdateRequest
from datadog_api_client.v2.model.twilio_basic_auth import TwilioBasicAuth
from datadog_api_client.v2.model.twilio_basic_auth_type import TwilioBasicAuthType
from datadog_api_client.v2.model.twilio_dataflow import TwilioDataflow
from datadog_api_client.v2.model.twilio_dataflow_id import TwilioDataflowId
from datadog_api_client.v2.model.twilio_integration_type import TwilioIntegrationType
from datadog_api_client.v2.model.twilio_integration_update import TwilioIntegrationUpdate
from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType
from datadog_api_client.v2.model.twilio_interface_update import TwilioInterfaceUpdate
from datadog_api_client.v2.model.twilio_settings_update import TwilioSettingsUpdate

body = IntegrationAccountUpdateRequest(
    data=IntegrationAccountUpdateData(
        attributes=IntegrationAccountUpdateAttributes(
            integration=TwilioIntegrationUpdate(
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
                type=TwilioIntegrationType.TWILIO,
            ),
            name="twilio-prod",
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = IntegrationAccountsApi(api_client)
    response = api_instance.update_integration_account(
        integration_id=IntegrationAccountIntegrationId.TWILIO,
        interface_id=IntegrationAccountInterfaceId.TWILIO,
        account_id="account_id",
        body=body,
    )

    print(response)
