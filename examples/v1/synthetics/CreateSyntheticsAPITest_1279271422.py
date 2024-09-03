"""
Create an API test with multi subtype returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_step import SyntheticsAPITestStep
from datadog_api_client.v1.model.synthetics_api_test_step_subtype import SyntheticsAPITestStepSubtype
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_api_wait_step import SyntheticsAPIWaitStep
from datadog_api_client.v1.model.synthetics_api_wait_step_subtype import SyntheticsAPIWaitStepSubtype
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType
from datadog_api_client.v1.model.synthetics_global_variable_parser_type import SyntheticsGlobalVariableParserType
from datadog_api_client.v1.model.synthetics_local_variable_parsing_options_type import (
    SyntheticsLocalVariableParsingOptionsType,
)
from datadog_api_client.v1.model.synthetics_parsing_options import SyntheticsParsingOptions
from datadog_api_client.v1.model.synthetics_test_call_type import SyntheticsTestCallType
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_metadata import SyntheticsTestMetadata
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_http_version import SyntheticsTestOptionsHTTPVersion
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
            SyntheticsAPITestStep(
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
                        type=SyntheticsLocalVariableParsingOptionsType.HTTP_HEADER,
                        secure=True,
                    ),
                ],
                is_critical=True,
                name="request is sent",
                request=SyntheticsTestRequest(
                    method="GET",
                    timeout=10.0,
                    url="https://datadoghq.com",
                    http_version=SyntheticsTestOptionsHTTPVersion.HTTP2,
                ),
                retry=SyntheticsTestOptionsRetry(
                    count=5,
                    interval=1000.0,
                ),
                subtype=SyntheticsAPITestStepSubtype.HTTP,
            ),
            SyntheticsAPIWaitStep(
                name="Wait",
                subtype=SyntheticsAPIWaitStepSubtype.WAIT,
                value=1,
            ),
            SyntheticsAPITestStep(
                name="GRPC CALL",
                subtype=SyntheticsAPITestStepSubtype.GRPC,
                extracted_values=[],
                allow_failure=False,
                is_critical=True,
                retry=SyntheticsTestOptionsRetry(
                    count=0,
                    interval=300.0,
                ),
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.LESS_THAN,
                        type=SyntheticsAssertionType.RESPONSE_TIME,
                        target=1000,
                    ),
                ],
                request=SyntheticsTestRequest(
                    host="grpcbin.test.k6.io",
                    port="9000",
                    service="grpcbin.GRPCBin",
                    method="Index",
                    message="{}",
                    compressed_json_descriptor="eJy1lU1z2yAQhv+Lzj74I3ETH506bQ7OZOSm1w4Wa4epBARQppqM/3v5koCJJdvtxCdW77vPssCO3zMKUgHOFu/ZXvBiS6hZho/f8qe7pftYgXphWJrlA8XwxywEvNba+6PhkC2yVcVVswYp0R6ykRYlZ1SCV21SDrxsssPIeS9FJKqGfK2rqnmmSBwhWa2XlKgtaQPiDcRGCUDVfwGD2sKUqKEtc1cSoOrsMlaMOec1sySYCCgUYRSVLv2zSva2u+FQkB0pVkIw8bFuIudOOn3pOaKYVT3Iy97Pd0AYhOx5QcMsnxvRHlnuLf8ETDd3CNtrv2nejkDpRnANCmGkkFn/hsYzpBKE7jVbufgnKnV9HRM9zRPDDKPttYT61n0TdWkAAjggk9AhuxIeaXd69CYTcsGw7cBTakLVbNpRzGEgyWjkSOpMbZXkhGL6oX30R49qt3GoHrap7i0XdD41WQ+2icCNm5p1hmFqnHNlcla0riKmDZ183crDxChjbnurtxHPRE784sVhWvDfGP+SsTKibU3o5NtWHuZFGZOxP6P5VXqIOvaOSec4eYohyd7NslHuJbd1bewds85xYrNxkr2d+5IhFWF3NvaO684xjE2S5ulY+tu64Pna0fCPJgzw6vF5/WucLcYjt5xoq19O3UDptOg/OamJQRaCcPPnMTQ2QDFn+uhPvUfnCrMc99upyQY4Ui9Dlc/YoG3R/v4Cs9YE+g==",
                    metadata=SyntheticsTestMetadata(),
                    call_type=SyntheticsTestCallType.UNARY,
                ),
            ),
        ],
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_test_multi_step_payload.json",
    name="Example-Synthetic",
    options=SyntheticsTestOptions(
        accept_self_signed=False,
        allow_insecure=True,
        follow_redirects=True,
        min_failure_duration=10,
        min_location_failed=1,
        monitor_name="Example-Synthetic",
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
