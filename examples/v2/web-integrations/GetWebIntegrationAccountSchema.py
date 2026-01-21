"""
Get account schema for an integration returns "OK: The JSON schema for the integration's account configuration."
response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.web_integrations_api import WebIntegrationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WebIntegrationsApi(api_client)
    response = api_instance.get_web_integration_account_schema(
        integration_name="integration_name",
    )

    print(response)
