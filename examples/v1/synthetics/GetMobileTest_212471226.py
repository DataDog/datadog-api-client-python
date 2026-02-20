"""
Get a Mobile test returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

# there is a valid "synthetics_mobile_test" in the system
SYNTHETICS_MOBILE_TEST_PUBLIC_ID = environ["SYNTHETICS_MOBILE_TEST_PUBLIC_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_mobile_test(
        public_id=SYNTHETICS_MOBILE_TEST_PUBLIC_ID,
    )

    print(response)
