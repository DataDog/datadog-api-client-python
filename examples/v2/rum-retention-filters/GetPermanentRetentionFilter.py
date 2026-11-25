"""
Get a permanent RUM retention filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RUMRetentionFiltersApi
from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RUMPermanentRetentionFilterID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersApi(api_client)
    response = api_instance.get_permanent_retention_filter(
        app_id="app_id",
        permanent_rf_id=RUMPermanentRetentionFilterID.SYNTHETICS_SESSIONS,
    )

    print(response)
