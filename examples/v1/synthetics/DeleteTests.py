"""
Delete tests returns "OK." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_delete_tests_payload import SyntheticsDeleteTestsPayload

# there is a valid "synthetics_api_test" in the system
SYNTHETICS_API_TEST_PUBLIC_ID = environ["SYNTHETICS_API_TEST_PUBLIC_ID"]

body = SyntheticsDeleteTestsPayload(
    public_ids=[
        SYNTHETICS_API_TEST_PUBLIC_ID,
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.delete_tests(body=body)

    print(response)
