"""
Delete a RUM retention filter returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

# there is a valid "rum_retention_filter" in the system
RUM_RETENTION_FILTER_DATA_ID = environ["RUM_RETENTION_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    api_instance.delete_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
        rf_id=RUM_RETENTION_FILTER_DATA_ID,
    )
