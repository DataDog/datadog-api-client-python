"""
Create a browser test returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_browser_test import SyntheticsBrowserTest
from datadog_api_client.v1.model.synthetics_browser_test_config import SyntheticsBrowserTestConfig
from datadog_api_client.v1.model.synthetics_browser_test_type import SyntheticsBrowserTestType
from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType
from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
from datadog_api_client.v1.model.synthetics_step import SyntheticsStep
from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

body = SyntheticsBrowserTest(
    config=SyntheticsBrowserTestConfig(
        assertions=[],
        config_variables=[
            SyntheticsConfigVariable(
                example="content-type",
                name="PROPERTY",
                pattern="content-type",
                type=SyntheticsConfigVariableType.TEXT,
                secure=True,
            ),
        ],
        request=SyntheticsTestRequest(
            method="GET",
            url="https://datadoghq.com",
        ),
        set_cookie="name:test",
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="Test message",
    name="Example-Create_a_browser_test_returns_OK_Returns_the_created_test_details_response",
    options=SyntheticsTestOptions(
        accept_self_signed=False,
        allow_insecure=True,
        device_ids=[
            SyntheticsDeviceID.TABLET,
        ],
        disable_cors=True,
        follow_redirects=True,
        min_failure_duration=10,
        min_location_failed=1,
        no_screenshot=True,
        retry=SyntheticsTestOptionsRetry(
            count=3,
            interval=10.0,
        ),
        tick_every=300,
    ),
    tags=[
        "testing:browser",
    ],
    type=SyntheticsBrowserTestType.BROWSER,
    steps=[
        SyntheticsStep(
            allow_failure=False,
            is_critical=True,
            name="Refresh page",
            params=dict(),
            type=SyntheticsStepType.REFRESH,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_browser_test(body=body)

    print(response)
