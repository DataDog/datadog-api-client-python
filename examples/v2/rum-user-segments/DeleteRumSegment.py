"""
Delete a RUM segment returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_user_segments_api import RUMUserSegmentsApi

configuration = Configuration()
configuration.unstable_operations["delete_rum_segment"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMUserSegmentsApi(api_client)
    response = api_instance.delete_rum_segment(
        segment_id="a1b2c3d4-1234-5678-9abc-123456789abc",
    )

    print(response)
