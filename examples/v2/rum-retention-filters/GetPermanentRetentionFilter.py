"""
Get a permanent RUM retention filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RumPermanentRetentionFilterID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.get_permanent_retention_filter(
        app_id="app_id",
        permanent_rf_id=RumPermanentRetentionFilterID.SYNTHETICS_SESSIONS,
    )

    print(response)
