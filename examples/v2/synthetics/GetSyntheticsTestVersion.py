"""
Get a specific version of a test returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_synthetics_test_version(
        public_id="public_id",
        version_number=9223372036854775807,
    )

    print(response)
