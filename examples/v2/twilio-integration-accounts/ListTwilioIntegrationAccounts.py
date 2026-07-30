"""
List Twilio integration accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_accounts_api import TwilioIntegrationAccountsApi
from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType

configuration = Configuration()
configuration.unstable_operations["list_twilio_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationAccountsApi(api_client)
    response = api_instance.list_twilio_integration_accounts(
        interface_id=TwilioInterfaceType.TWILIO,
    )

    print(response)
