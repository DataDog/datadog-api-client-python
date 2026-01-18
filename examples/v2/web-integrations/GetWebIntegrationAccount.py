"""
Get integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi

# there is a valid "web_integration_account" in the system
WEB_INTEGRATION_ACCOUNT_DATA_ID = environ["WEB_INTEGRATION_ACCOUNT_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.get_web_integration_account(
        integration_name="twilio",
        account_id=WEB_INTEGRATION_ACCOUNT_DATA_ID,
    )

    print(response)
