"""
Create an API test returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_browser_test_rum_settings import SyntheticsBrowserTestRumSettings
from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles
from datadog_api_client.v1.model.synthetics_test_ci_options import SyntheticsTestCiOptions
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_execution_rule import SyntheticsTestExecutionRule
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        assertions=[
            SyntheticsAssertionTarget(
                operator=SyntheticsAssertionOperator.LESS_THAN,
                target=1000,
                type=SyntheticsAssertionType.RESPONSE_TIME,
            ),
        ],
        request=SyntheticsTestRequest(
            method="GET",
            url="https://example.com",
        ),
    ),
    locations=[
        "aws:eu-west-3",
    ],
    message="Notification message",
    name="Example test name",
    options=SyntheticsTestOptions(
        ci=SyntheticsTestCiOptions(
            execution_rule=SyntheticsTestExecutionRule.BLOCKING,
        ),
        device_ids=[
            SyntheticsDeviceID.LAPTOP_LARGE,
        ],
        monitor_options=SyntheticsTestOptionsMonitorOptions(),
        restricted_roles=SyntheticsRestrictedRoles(
            [
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            ]
        ),
        retry=SyntheticsTestOptionsRetry(),
        rum_settings=SyntheticsBrowserTestRumSettings(
            application_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            client_token_id=12345,
            is_enabled=True,
        ),
    ),
    status=SyntheticsTestPauseStatus.LIVE,
    subtype=SyntheticsTestDetailsSubType.HTTP,
    tags=[
        "env:production",
    ],
    type=SyntheticsAPITestType.API,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_api_test(body=body)

    print(response)
