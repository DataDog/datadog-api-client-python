"""
Create an API GRPC test returns "OK - Returns the created test details." response
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
from datadog_api_client.v1.model.synthetics_test_metadata import SyntheticsTestMetadata
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        assertions=[
            SyntheticsAssertionTarget(
                operator=SyntheticsAssertionOperator.IS,
                target=1,
                type=SyntheticsAssertionType.GRPC_HEALTHCHECK_STATUS,
            ),
        ],
        request=SyntheticsTestRequest(
            host="localhost",
            port=50051,
            service="Hello",
            method="GET",
            message="",
            metadata=SyntheticsTestMetadata(),
        ),
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_grpc_test_payload.json",
    name="Example-Create_an_API_GRPC_test_returns_OK_Returns_the_created_test_details_response",
    options=SyntheticsTestOptions(
        min_failure_duration=0,
        min_location_failed=1,
        monitor_options=SyntheticsTestOptionsMonitorOptions(
            renotify_interval=0,
        ),
        monitor_name="Example-Create_an_API_GRPC_test_returns_OK_Returns_the_created_test_details_response",
        tick_every=60,
    ),
    subtype=SyntheticsTestDetailsSubType.GRPC,
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
