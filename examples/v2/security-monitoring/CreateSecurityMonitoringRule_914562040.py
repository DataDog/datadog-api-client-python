"""
Create a detection rule with type 'signal_correlation' returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
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
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_signal_rule_create_payload import (
    SecurityMonitoringSignalRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_signal_rule_query import SecurityMonitoringSignalRuleQuery
from datadog_api_client.v2.model.security_monitoring_signal_rule_type import SecurityMonitoringSignalRuleType

# there is a valid "security_rule" in the system
SECURITY_RULE_ID = environ["SECURITY_RULE_ID"]

# there is a valid "security_rule_bis" in the system
SECURITY_RULE_BIS_ID = environ["SECURITY_RULE_BIS_ID"]

body = SecurityMonitoringSignalRuleCreatePayload(
    name="Example-Create_a_detection_rule_with_type_signal_correlation_returns_OK_response_signal_rule",
    queries=[
        SecurityMonitoringSignalRuleQuery(
            rule_id=SECURITY_RULE_ID,
            aggregation=SecurityMonitoringRuleQueryAggregation.EVENT_COUNT,
            correlated_by_fields=[
                "host",
            ],
            correlated_query_index=1,
        ),
        SecurityMonitoringSignalRuleQuery(
            rule_id=SECURITY_RULE_BIS_ID,
            aggregation=SecurityMonitoringRuleQueryAggregation.EVENT_COUNT,
            correlated_by_fields=[
                "host",
            ],
        ),
    ],
    filters=[],
    cases=[
        SecurityMonitoringRuleCaseCreate(
            name="",
            status=SecurityMonitoringRuleSeverity.INFO,
            condition="a > 0 && b > 0",
            notifications=[],
        ),
    ],
    options=SecurityMonitoringRuleOptions(
        evaluation_window=SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES,
        keep_alive=SecurityMonitoringRuleKeepAlive.ONE_HOUR,
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ONE_DAY,
    ),
    message="Test signal correlation rule",
    tags=[],
    is_enabled=True,
    type=SecurityMonitoringSignalRuleType.SIGNAL_CORRELATION,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
