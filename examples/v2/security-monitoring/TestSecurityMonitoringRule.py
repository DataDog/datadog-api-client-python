"""
Test a rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
from datadog_api_client.v2.model.security_monitoring_rule_detection_method import SecurityMonitoringRuleDetectionMethod
from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
    SecurityMonitoringRuleEvaluationWindow,
)
from datadog_api_client.v2.model.security_monitoring_rule_keep_alive import SecurityMonitoringRuleKeepAlive
from datadog_api_client.v2.model.security_monitoring_rule_max_signal_duration import (
    SecurityMonitoringRuleMaxSignalDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
    SecurityMonitoringRuleQueryAggregation,
)
from datadog_api_client.v2.model.security_monitoring_rule_query_payload import SecurityMonitoringRuleQueryPayload
from datadog_api_client.v2.model.security_monitoring_rule_query_payload_data import (
    SecurityMonitoringRuleQueryPayloadData,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_test_request import SecurityMonitoringRuleTestRequest
from datadog_api_client.v2.model.security_monitoring_rule_type_test import SecurityMonitoringRuleTypeTest
from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery
from datadog_api_client.v2.model.security_monitoring_standard_rule_test_payload import (
    SecurityMonitoringStandardRuleTestPayload,
)

body = SecurityMonitoringRuleTestRequest(
    rule=SecurityMonitoringStandardRuleTestPayload(
        cases=[
            SecurityMonitoringRuleCaseCreate(
                name="",
                status=SecurityMonitoringRuleSeverity.INFO,
                notifications=[],
                condition="a > 0",
            ),
        ],
        has_extended_title=True,
        is_enabled=True,
        message="My security monitoring rule message.",
        name="My security monitoring rule.",
        options=SecurityMonitoringRuleOptions(
            decrease_criticality_based_on_env=False,
            detection_method=SecurityMonitoringRuleDetectionMethod.THRESHOLD,
            evaluation_window=SecurityMonitoringRuleEvaluationWindow.ZERO_MINUTES,
            keep_alive=SecurityMonitoringRuleKeepAlive.ZERO_MINUTES,
            max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ZERO_MINUTES,
        ),
        queries=[
            SecurityMonitoringStandardRuleQuery(
                query="source:source_here",
                group_by_fields=[
                    "@userIdentity.assumed_role",
                ],
                distinct_fields=[],
                aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
                name="",
            ),
        ],
        tags=[
            "env:prod",
            "team:security",
        ],
        type=SecurityMonitoringRuleTypeTest.LOG_DETECTION,
    ),
    rule_query_payloads=[
        SecurityMonitoringRuleQueryPayload(
            expected_result=True,
            index=0,
            payload=SecurityMonitoringRuleQueryPayloadData(
                ddsource="source_here",
                ddtags="env:staging,version:5.1",
                hostname="i-012345678",
                message="2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World",
                service="payment",
                user_identity=dict([("assumed_role", "fake assumed_role")]),
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.test_security_monitoring_rule(body=body)

    print(response)
