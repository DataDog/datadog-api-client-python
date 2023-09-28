"""
Get a given APM retention filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi

# there is a valid "retention_filter" in the system
RETENTION_FILTER_DATA_ID = environ["RETENTION_FILTER_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.get_apm_retention_filter(
        filter_id=RETENTION_FILTER_DATA_ID,
    )

    print(response)
