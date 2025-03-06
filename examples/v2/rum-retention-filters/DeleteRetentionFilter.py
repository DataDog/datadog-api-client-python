"""
Delete a RUM retention filter returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    api_instance.delete_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
        rf_id="fe34ee09-14cf-4976-9362-08044c0dea80",
    )
