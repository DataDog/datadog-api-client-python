"""
Delete a RUM exclusion filter returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    api_instance.delete_exclusion_filter(
        app_id="app_id",
        ef_id="ef_id",
    )
