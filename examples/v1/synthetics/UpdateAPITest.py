"""
Edit an API test returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_assertion_json_path_operator import SyntheticsAssertionJSONPathOperator
from datadog_api_client.v1.model.synthetics_assertion_json_path_target import SyntheticsAssertionJSONPathTarget
from datadog_api_client.v1.model.synthetics_assertion_json_path_target_target import (
    SyntheticsAssertionJSONPathTargetTarget,
)
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate
from datadog_api_client.v1.model.synthetics_test_request_certificate_item import SyntheticsTestRequestCertificateItem

# there is a valid "synthetics_api_test" in the system
SYNTHETICS_API_TEST_PUBLIC_ID = environ["SYNTHETICS_API_TEST_PUBLIC_ID"]

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        assertions=[
            SyntheticsAssertionTarget(
                operator=SyntheticsAssertionOperator.IS,
                _property="{{ PROPERTY }}",
                target="text/html",
                type=SyntheticsAssertionType.HEADER,
            ),
            SyntheticsAssertionTarget(
                operator=SyntheticsAssertionOperator.LESS_THAN,
                target=2000,
                type=SyntheticsAssertionType.RESPONSE_TIME,
            ),
            SyntheticsAssertionJSONPathTarget(
                operator=SyntheticsAssertionJSONPathOperator.VALIDATES_JSON_PATH,
                target=SyntheticsAssertionJSONPathTargetTarget(
                    json_path="topKey",
                    operator="isNot",
                    target_value="0",
                ),
                type=SyntheticsAssertionType.BODY,
            ),
        ],
        config_variables=[
            SyntheticsConfigVariable(
                example="content-type",
                name="PROPERTY",
                pattern="content-type",
                type=SyntheticsConfigVariableType.TEXT,
            ),
        ],
        request=SyntheticsTestRequest(
            certificate=SyntheticsTestRequestCertificate(
                cert=SyntheticsTestRequestCertificateItem(
                    filename="cert-filename",
                    updated_at="2020-10-16T09:23:24.857Z",
                ),
                key=SyntheticsTestRequestCertificateItem(
                    filename="key-filename",
                    updated_at="2020-10-16T09:23:24.857Z",
                ),
            ),
            headers=SyntheticsTestHeaders(
                unique="exampleeditanapitestreturnsokresponse",
            ),
            method="GET",
            timeout=10.0,
            url="https://datadoghq.com",
        ),
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_test_payload.json",
    name="Example-Edit_an_API_test_returns_OK_response-updated",
    options=SyntheticsTestOptions(
        accept_self_signed=False,
        allow_insecure=True,
        follow_redirects=True,
        min_failure_duration=10,
        min_location_failed=1,
        monitor_name="Test-TestSyntheticsAPITestLifecycle-1623076664",
        monitor_priority=5,
        retry=SyntheticsTestOptionsRetry(
            count=3,
            interval=10.0,
        ),
        tick_every=60,
    ),
    status=SyntheticsTestPauseStatus.LIVE,
    subtype=SyntheticsTestDetailsSubType.HTTP,
    tags=[
        "testing:api",
    ],
    type=SyntheticsAPITestType.API,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.update_api_test(public_id=SYNTHETICS_API_TEST_PUBLIC_ID, body=body)

    print(response)
