"""
Create a Network Path test returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.synthetics_network_assertion_latency import SyntheticsNetworkAssertionLatency
from datadog_api_client.v2.model.synthetics_network_assertion_latency_type import SyntheticsNetworkAssertionLatencyType
from datadog_api_client.v2.model.synthetics_network_assertion_operator import SyntheticsNetworkAssertionOperator
from datadog_api_client.v2.model.synthetics_network_assertion_property import SyntheticsNetworkAssertionProperty
from datadog_api_client.v2.model.synthetics_network_test import SyntheticsNetworkTest
from datadog_api_client.v2.model.synthetics_network_test_config import SyntheticsNetworkTestConfig
from datadog_api_client.v2.model.synthetics_network_test_edit import SyntheticsNetworkTestEdit
from datadog_api_client.v2.model.synthetics_network_test_edit_request import SyntheticsNetworkTestEditRequest
from datadog_api_client.v2.model.synthetics_network_test_request import SyntheticsNetworkTestRequest
from datadog_api_client.v2.model.synthetics_network_test_request_tcp_method import SyntheticsNetworkTestRequestTCPMethod
from datadog_api_client.v2.model.synthetics_network_test_sub_type import SyntheticsNetworkTestSubType
from datadog_api_client.v2.model.synthetics_network_test_type import SyntheticsNetworkTestType
from datadog_api_client.v2.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v2.model.synthetics_test_pause_status import SyntheticsTestPauseStatus

body = SyntheticsNetworkTestEditRequest(
    data=SyntheticsNetworkTestEdit(
        attributes=SyntheticsNetworkTest(
            config=SyntheticsNetworkTestConfig(
                assertions=[
                    SyntheticsNetworkAssertionLatency(
                        operator=SyntheticsNetworkAssertionOperator.LESS_THAN,
                        _property=SyntheticsNetworkAssertionProperty.AVG,
                        target=500.0,
                        type=SyntheticsNetworkAssertionLatencyType.LATENCY,
                    ),
                ],
                request=SyntheticsNetworkTestRequest(
                    host="example.com",
                    port=443,
                    tcp_method=SyntheticsNetworkTestRequestTCPMethod.PREFER_SACK,
                    max_ttl=30,
                    e2e_queries=50,
                    traceroute_queries=3,
                ),
            ),
            locations=[
                "aws:us-east-1",
                "agent:my-agent-name",
            ],
            message="Network Path test notification",
            name="Example Network Path test",
            options=SyntheticsTestOptions(
                tick_every=60,
            ),
            status=SyntheticsTestPauseStatus.LIVE,
            subtype=SyntheticsNetworkTestSubType.TCP,
            tags=[
                "env:production",
            ],
            type=SyntheticsNetworkTestType.NETWORK,
        ),
        type=SyntheticsNetworkTestType.NETWORK,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_network_test(body=body)

    print(response)
