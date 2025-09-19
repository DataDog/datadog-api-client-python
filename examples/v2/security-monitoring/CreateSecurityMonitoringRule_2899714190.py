"""
Create a detection rule with detection method 'sequence_detection' returns "OK" response
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
from datadog_api_client.v2.model.security_monitoring_rule_sequence_detection_options import (
    SecurityMonitoringRuleSequenceDetectionOptions,
)
from datadog_api_client.v2.model.security_monitoring_rule_sequence_detection_step import (
    SecurityMonitoringRuleSequenceDetectionStep,
)
from datadog_api_client.v2.model.security_monitoring_rule_sequence_detection_step_transition import (
    SecurityMonitoringRuleSequenceDetectionStepTransition,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate
from datadog_api_client.v2.model.security_monitoring_standard_data_source import SecurityMonitoringStandardDataSource
from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
    SecurityMonitoringStandardRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery

body = SecurityMonitoringStandardRuleCreatePayload(
    name="Example-Security-Monitoring",
    type=SecurityMonitoringRuleTypeCreate.LOG_DETECTION,
    is_enabled=True,
    queries=[
        SecurityMonitoringStandardRuleQuery(
            aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
            data_source=SecurityMonitoringStandardDataSource.LOGS,
            distinct_fields=[],
            group_by_fields=[],
            has_optional_group_by_fields=False,
            name="",
            query="service:logs-rule-reducer source:paul test2",
        ),
        SecurityMonitoringStandardRuleQuery(
            aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
            data_source=SecurityMonitoringStandardDataSource.LOGS,
            distinct_fields=[],
            group_by_fields=[],
            has_optional_group_by_fields=False,
            name="",
            query="service:logs-rule-reducer source:paul test1",
        ),
    ],
    cases=[
        SecurityMonitoringRuleCaseCreate(
            name="",
            status=SecurityMonitoringRuleSeverity.INFO,
            notifications=[],
            condition="step_b > 0",
        ),
    ],
    message="Logs and signals asdf",
    options=SecurityMonitoringRuleOptions(
        detection_method=SecurityMonitoringRuleDetectionMethod.SEQUENCE_DETECTION,
        evaluation_window=SecurityMonitoringRuleEvaluationWindow.ZERO_MINUTES,
        keep_alive=SecurityMonitoringRuleKeepAlive.FIVE_MINUTES,
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.TEN_MINUTES,
        sequence_detection_options=SecurityMonitoringRuleSequenceDetectionOptions(
            step_transitions=[
                SecurityMonitoringRuleSequenceDetectionStepTransition(
                    child="step_b",
                    evaluation_window=SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES,
                    parent="step_a",
                ),
            ],
            steps=[
                SecurityMonitoringRuleSequenceDetectionStep(
                    condition="a > 0",
                    evaluation_window=SecurityMonitoringRuleEvaluationWindow.ONE_MINUTE,
                    name="step_a",
                ),
                SecurityMonitoringRuleSequenceDetectionStep(
                    condition="b > 0",
                    evaluation_window=SecurityMonitoringRuleEvaluationWindow.ONE_MINUTE,
                    name="step_b",
                ),
            ],
        ),
    ),
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
