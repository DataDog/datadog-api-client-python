"""
Create an API test with WEBSOCKET subtype returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        assertions=[
            SyntheticsAssertionTarget(
                operator=SyntheticsAssertionOperator.IS,
                target="message",
                type=SyntheticsAssertionType.RECEIVED_MESSAGE,
            ),
            SyntheticsAssertionTarget(
                operator=SyntheticsAssertionOperator.LESS_THAN,
                target=2000,
                type=SyntheticsAssertionType.RESPONSE_TIME,
            ),
        ],
        config_variables=[],
        request=SyntheticsTestRequest(
            url="ws://datadoghq.com",
            message="message",
        ),
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_test_websocket_payload.json",
    name="Example-Create_an_API_test_with_WEBSOCKET_subtype_returns_OK_Returns_the_created_test_details_response",
    options=SyntheticsTestOptions(
        accept_self_signed=False,
        allow_insecure=True,
        follow_redirects=True,
        min_failure_duration=10,
        min_location_failed=1,
        monitor_name="Example-Create_an_API_test_with_WEBSOCKET_subtype_returns_OK_Returns_the_created_test_details_response",
        monitor_priority=5,
        retry=SyntheticsTestOptionsRetry(
            count=3,
            interval=10.0,
        ),
        tick_every=60,
    ),
    subtype=SyntheticsTestDetailsSubType.WEBSOCKET,
    tags=[
        "testing:api",
    ],
    type=SyntheticsAPITestType.API,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_api_test(body=body)

    print(response)
