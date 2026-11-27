"""
Get a RUM exclusion filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

# there is a valid "rum_exclusion_filter" in the system
RUM_EXCLUSION_FILTER_DATA_ID = environ["RUM_EXCLUSION_FILTER_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.get_exclusion_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
        ef_id=RUM_EXCLUSION_FILTER_DATA_ID,
    )

    print(response)
