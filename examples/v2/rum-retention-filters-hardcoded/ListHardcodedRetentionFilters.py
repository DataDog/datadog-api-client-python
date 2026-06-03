"""
Get all hardcoded retention filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_hardcoded_api import RUMRetentionFiltersHardcodedApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersHardcodedApi(api_client)
    response = api_instance.list_hardcoded_retention_filters(
        app_id="Example-RUM-Retention-Filters-Hardcoded",
    )

    print(response)
