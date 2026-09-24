"""
Get all connected Salesforce organizations returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.salesforce_integration_api import SalesforceIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SalesforceIntegrationApi(api_client)
    response = api_instance.get_salesforce_organizations()

    print(response)
