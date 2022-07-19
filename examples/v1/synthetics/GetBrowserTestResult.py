"""
Get a browser test result returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_browser_test_result(
        public_id="2yy-sem-mjh",
        result_id="5671719892074090418",
    )

    print(response)
