"""
Remove a test from a Synthetics downtime returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.remove_test_from_synthetics_downtime(
        downtime_id="00000000-0000-0000-0000-000000000001",
        test_id="abc-def-123",
    )

    print(response)
