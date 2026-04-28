"""
Delete a Synthetics downtime returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    api_instance.delete_synthetics_downtime(
        downtime_id="00000000-0000-0000-0000-000000000001",
    )
