"""
Create a multistep test with subtest returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_subtest_step import SyntheticsAPISubtestStep
from datadog_api_client.v1.model.synthetics_api_subtest_step_subtype import SyntheticsAPISubtestStepSubtype
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_step import SyntheticsAPITestStep
from datadog_api_client.v1.model.synthetics_api_test_step_subtype import SyntheticsAPITestStepSubtype
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_basic_auth_web import SyntheticsBasicAuthWeb
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

# there is a valid "synthetics_api_test" in the system
SYNTHETICS_API_TEST_PUBLIC_ID = environ["SYNTHETICS_API_TEST_PUBLIC_ID"]

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        steps=[
            SyntheticsAPITestStep(
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                name="request is sent",
                request=SyntheticsTestRequest(
                    url="https://httpbin.org/status/200",
                    method="GET",
                    basic_auth=SyntheticsBasicAuthWeb(
                        password="password",
                        username="username",
                    ),
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPISubtestStep(
                subtype=SyntheticsAPISubtestStepSubtype.PLAY_SUB_TEST,
                subtest_public_id=SYNTHETICS_API_TEST_PUBLIC_ID,
                name="subtest step",
            ),
        ],
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_test_multi_step_with_subtest.json",
    name="Example-Synthetic",
    options=SyntheticsTestOptions(
        tick_every=60,
    ),
    subtype=SyntheticsTestDetailsSubType.MULTI,
    type=SyntheticsAPITestType.API,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_api_test(body=body)

    print(response)
