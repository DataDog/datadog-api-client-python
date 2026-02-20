"""
Edit a Network Path test returns "OK" response
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
from datadog_api_client.v2.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
from datadog_api_client.v2.model.synthetics_test_options_monitor_options_notification_preset_name import (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName,
)
from datadog_api_client.v2.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v2.model.synthetics_test_options_scheduling import SyntheticsTestOptionsScheduling
from datadog_api_client.v2.model.synthetics_test_options_scheduling_timeframe import (
    SyntheticsTestOptionsSchedulingTimeframe,
)
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
                    e2e_queries=50,
                    host="",
                    max_ttl=30,
                    port=443,
                    tcp_method=SyntheticsNetworkTestRequestTCPMethod.PREFER_SACK,
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
                monitor_options=SyntheticsTestOptionsMonitorOptions(
                    notification_preset_name=SyntheticsTestOptionsMonitorOptionsNotificationPresetName.SHOW_ALL,
                ),
                restricted_roles=[
                    "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                ],
                retry=SyntheticsTestOptionsRetry(),
                scheduling=SyntheticsTestOptionsScheduling(
                    timeframes=[
                        SyntheticsTestOptionsSchedulingTimeframe(
                            day=1,
                            _from="07:00",
                            to="16:00",
                        ),
                        SyntheticsTestOptionsSchedulingTimeframe(
                            day=3,
                            _from="07:00",
                            to="16:00",
                        ),
                    ],
                    timezone="America/New_York",
                ),
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
    response = api_instance.update_synthetics_network_test(public_id="public_id", body=body)

    print(response)
