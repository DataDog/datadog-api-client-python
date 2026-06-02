"""
Get a hardcoded retention filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_hardcoded_api import RUMRetentionFiltersHardcodedApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersHardcodedApi(api_client)
    response = api_instance.get_hardcoded_retention_filter(
        app_id="Example-RUM-Retention-Filters-Hardcoded",
        rf_id="Example-RUM-Retention-Filters-Hardcoded",
    )

    print(response)
