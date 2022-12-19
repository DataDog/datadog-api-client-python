"""
Create an API test with multi subtype returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_step import SyntheticsAPIStep
from datadog_api_client.v1.model.synthetics_api_step_subtype import SyntheticsAPIStepSubtype
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options_type import (
    SyntheticsGlobalVariableParseTestOptionsType,
)
from datadog_api_client.v1.model.synthetics_global_variable_parser_type import SyntheticsGlobalVariableParserType
from datadog_api_client.v1.model.synthetics_parsing_options import SyntheticsParsingOptions
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
from datadog_api_client.v1.model.synthetics_variable_parser import SyntheticsVariableParser

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        config_variables=[
            SyntheticsConfigVariable(
                example="content-type",
                name="PROPERTY",
                pattern="content-type",
                type=SyntheticsConfigVariableType.TEXT,
            ),
        ],
        steps=[
            SyntheticsAPIStep(
                allow_failure=True,
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                ],
                extracted_values=[
                    SyntheticsParsingOptions(
                        field="server",
                        name="EXTRACTED_VALUE",
                        parser=SyntheticsVariableParser(
                            type=SyntheticsGlobalVariableParserType.RAW,
                        ),
                        type=SyntheticsGlobalVariableParseTestOptionsType.HTTP_HEADER,
                    ),
                ],
                is_critical=True,
                name="request is sent",
                request=SyntheticsTestRequest(
                    method="GET",
                    timeout=10.0,
                    url="https://datadoghq.com",
                ),
                retry=SyntheticsTestOptionsRetry(
                    count=5,
                    interval=1000.0,
                ),
                subtype=SyntheticsAPIStepSubtype.HTTP,
            ),
        ],
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_test_multi_step_payload.json",
    name="Example-Create_an_API_test_with_multi_subtype_returns_OK_Returns_the_created_test_details_response",
    options=SyntheticsTestOptions(
        accept_self_signed=False,
        allow_insecure=True,
        follow_redirects=True,
        min_failure_duration=10,
        min_location_failed=1,
        monitor_name="Example-Create_an_API_test_with_multi_subtype_returns_OK_Returns_the_created_test_details_response",
        monitor_priority=5,
        retry=SyntheticsTestOptionsRetry(
            count=3,
            interval=1000.0,
        ),
        tick_every=60,
    ),
    subtype=SyntheticsTestDetailsSubType.MULTI,
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
