"""
Delete a Twilio integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_api import TwilioIntegrationApi

configuration = Configuration()
configuration.unstable_operations["delete_twilio_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationApi(api_client)
    api_instance.delete_twilio_integration_account(
        account_id="account_id",
    )
