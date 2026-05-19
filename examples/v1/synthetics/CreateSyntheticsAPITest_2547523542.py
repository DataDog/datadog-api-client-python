"""
Create an API test with MCP steps returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_step import SyntheticsAPITestStep
from datadog_api_client.v1.model.synthetics_api_test_step_subtype import SyntheticsAPITestStepSubtype
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_assertion_mcp_respects_specification import (
    SyntheticsAssertionMCPRespectsSpecification,
)
from datadog_api_client.v1.model.synthetics_assertion_mcp_respects_specification_type import (
    SyntheticsAssertionMCPRespectsSpecificationType,
)
from datadog_api_client.v1.model.synthetics_assertion_mcp_server_capabilities_target import (
    SyntheticsAssertionMCPServerCapabilitiesTarget,
)
from datadog_api_client.v1.model.synthetics_assertion_mcp_server_capabilities_type import (
    SyntheticsAssertionMCPServerCapabilitiesType,
)
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_mcp_protocol_version import SyntheticsMCPProtocolVersion
from datadog_api_client.v1.model.synthetics_mcp_server_capability import SyntheticsMCPServerCapability
from datadog_api_client.v1.model.synthetics_test_call_type import SyntheticsTestCallType
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

body = SyntheticsAPITest(
    config=SyntheticsAPITestConfig(
        steps=[
            SyntheticsAPITestStep(
                name="Initialize MCP session",
                subtype=SyntheticsAPITestStepSubtype.MCP,
                allow_failure=False,
                is_critical=True,
                retry=SyntheticsTestOptionsRetry(
                    count=0,
                    interval=300.0,
                ),
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                    SyntheticsAssertionMCPRespectsSpecification(
                        type=SyntheticsAssertionMCPRespectsSpecificationType.MCP_RESPECTS_SPECIFICATION,
                    ),
                    SyntheticsAssertionMCPServerCapabilitiesTarget(
                        operator=SyntheticsAssertionOperator.CONTAINS,
                        type=SyntheticsAssertionMCPServerCapabilitiesType.MCP_SERVER_CAPABILITIES,
                        target=[
                            SyntheticsMCPServerCapability.TOOLS,
                        ],
                    ),
                ],
                request=SyntheticsTestRequest(
                    url="https://example.org/mcp",
                    call_type=SyntheticsTestCallType.INIT,
                    mcp_protocol_version=SyntheticsMCPProtocolVersion.VERSION_2025_06_18,
                    headers={
                        "DD-API-KEY": "<YOUR-API-KEY>",
                        "DD-APPLICATION-KEY": "<YOUR-APP-KEY>",
                    },
                ),
            ),
            SyntheticsAPITestStep(
                name="List MCP tools",
                subtype=SyntheticsAPITestStepSubtype.MCP,
                allow_failure=False,
                is_critical=True,
                retry=SyntheticsTestOptionsRetry(
                    count=0,
                    interval=300.0,
                ),
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.MORE_THAN,
                        type=SyntheticsAssertionType.MCP_TOOL_COUNT,
                        target=0,
                    ),
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.LESS_THAN,
                        type=SyntheticsAssertionType.MCP_TOOL_NAME_LENGTH,
                        target=64,
                    ),
                    SyntheticsAssertionMCPRespectsSpecification(
                        type=SyntheticsAssertionMCPRespectsSpecificationType.MCP_RESPECTS_SPECIFICATION,
                    ),
                ],
                request=SyntheticsTestRequest(
                    url="https://example.org/mcp",
                    call_type=SyntheticsTestCallType.TOOL_LIST,
                    mcp_protocol_version=SyntheticsMCPProtocolVersion.VERSION_2025_06_18,
                    headers={
                        "DD-API-KEY": "<YOUR-API-KEY>",
                        "DD-APPLICATION-KEY": "<YOUR-APP-KEY>",
                    },
                ),
            ),
            SyntheticsAPITestStep(
                name="Call MCP search tool",
                subtype=SyntheticsAPITestStepSubtype.MCP,
                allow_failure=False,
                is_critical=True,
                retry=SyntheticsTestOptionsRetry(
                    count=0,
                    interval=300.0,
                ),
                assertions=[
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.IS,
                        type=SyntheticsAssertionType.STATUS_CODE,
                        target=200,
                    ),
                    SyntheticsAssertionTarget(
                        operator=SyntheticsAssertionOperator.LESS_THAN,
                        type=SyntheticsAssertionType.RESPONSE_TIME,
                        target=5000,
                    ),
                    SyntheticsAssertionMCPRespectsSpecification(
                        type=SyntheticsAssertionMCPRespectsSpecificationType.MCP_RESPECTS_SPECIFICATION,
                    ),
                ],
                request=SyntheticsTestRequest(
                    url="https://example.org/mcp",
                    call_type=SyntheticsTestCallType.TOOL_CALL,
                    mcp_protocol_version=SyntheticsMCPProtocolVersion.VERSION_2025_06_18,
                    tool_name="search",
                    tool_args=dict([("limit", "5"), ("query", "datadog synthetics")]),
                    headers={
                        "DD-API-KEY": "<YOUR-API-KEY>",
                        "DD-APPLICATION-KEY": "<YOUR-APP-KEY>",
                    },
                ),
            ),
        ],
    ),
    locations=[
        "aws:us-east-2",
    ],
    message="BDD test payload: synthetics_api_test_mcp_payload.json",
    name="Example-Synthetic",
    options=SyntheticsTestOptions(
        min_failure_duration=10,
        min_location_failed=1,
        monitor_name="Example-Synthetic",
        monitor_priority=5,
        retry=SyntheticsTestOptionsRetry(
            count=3,
            interval=1000.0,
        ),
        tick_every=900,
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
