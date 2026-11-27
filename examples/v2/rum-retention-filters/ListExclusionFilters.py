"""
Get all RUM exclusion filters returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.list_exclusion_filters(
        app_id=RUM_APPLICATION_DATA_ID,
    )

    print(response)
