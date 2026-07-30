"""
Delete a Twilio integration account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_accounts_api import TwilioIntegrationAccountsApi
from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType

configuration = Configuration()
configuration.unstable_operations["delete_twilio_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationAccountsApi(api_client)
    api_instance.delete_twilio_integration_account(
        interface_id=TwilioInterfaceType.TWILIO,
        account_id="account_id",
    )
