"""
Get an API test result returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_api_test_result(
        public_id="hwb-332-3xe",
        result_id="3420446318379485707",
    )

    print(response)
