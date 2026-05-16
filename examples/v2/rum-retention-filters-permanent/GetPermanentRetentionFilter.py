"""
Get a permanent retention filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_permanent_api import RumRetentionFiltersPermanentApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersPermanentApi(api_client)
    response = api_instance.get_permanent_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690",
        rf_id="default_synthetics",
    )

    print(response)
