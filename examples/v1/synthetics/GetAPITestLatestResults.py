"""
Get an API test's latest results summaries returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_api_test_latest_results(
        public_id="hwb-332-3xe",
    )

    print(response)
