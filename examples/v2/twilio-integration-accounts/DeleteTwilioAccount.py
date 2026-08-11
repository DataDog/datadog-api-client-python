"""
Delete a Twilio integration account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_accounts_api import TwilioIntegrationAccountsApi

configuration = Configuration()
configuration.unstable_operations["delete_twilio_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationAccountsApi(api_client)
    api_instance.delete_twilio_account(
        account_id="account_id",
    )
