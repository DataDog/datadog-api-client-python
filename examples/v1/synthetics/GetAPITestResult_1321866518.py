"""
Get an API test result returns result with failure object
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

# there is a "synthetics_api_test_with_wrong_dns" in the system
SYNTHETICS_API_TEST_WITH_WRONG_DNS_PUBLIC_ID = environ["SYNTHETICS_API_TEST_WITH_WRONG_DNS_PUBLIC_ID"]

# the "synthetics_api_test_with_wrong_dns" is triggered
SYNTHETICS_API_TEST_WITH_WRONG_DNS_RESULT_RESULTS_0_RESULT_ID = environ[
    "SYNTHETICS_API_TEST_WITH_WRONG_DNS_RESULT_RESULTS_0_RESULT_ID"
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_api_test_result(
        public_id=SYNTHETICS_API_TEST_WITH_WRONG_DNS_PUBLIC_ID,
        result_id=SYNTHETICS_API_TEST_WITH_WRONG_DNS_RESULT_RESULTS_0_RESULT_ID,
    )

    print(response)
