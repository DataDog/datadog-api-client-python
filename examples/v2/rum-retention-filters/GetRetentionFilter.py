"""
Get a RUM retention filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.get_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
        rf_id="4b95d361-f65d-4515-9824-c9aaeba5ac2a",
    )

    print(response)
