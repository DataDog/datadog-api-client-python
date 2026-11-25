"""
Get all RUM retention filters returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RUMRetentionFiltersApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersApi(api_client)
    response = api_instance.list_retention_filters(
        app_id="1d4b9c34-7ac4-423a-91cf-9902d926e9b3",
    )

    print(response)
