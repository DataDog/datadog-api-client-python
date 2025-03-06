"""
Get all RUM retention filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.list_retention_filters(
        app_id="1d4b9c34-7ac4-423a-91cf-9902d926e9b3",
    )

    print(response)
