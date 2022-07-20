"""
Update an existing rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
from datadog_api_client.v2.model.security_monitoring_filter_action import SecurityMonitoringFilterAction
from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
from datadog_api_client.v2.model.security_monitoring_rule_detection_method import SecurityMonitoringRuleDetectionMethod
from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
    SecurityMonitoringRuleEvaluationWindow,
)
from datadog_api_client.v2.model.security_monitoring_rule_hardcoded_evaluator_type import (
    SecurityMonitoringRuleHardcodedEvaluatorType,
)
from datadog_api_client.v2.model.security_monitoring_rule_impossible_travel_options import (
    SecurityMonitoringRuleImpossibleTravelOptions,
)
from datadog_api_client.v2.model.security_monitoring_rule_keep_alive import SecurityMonitoringRuleKeepAlive
from datadog_api_client.v2.model.security_monitoring_rule_max_signal_duration import (
    SecurityMonitoringRuleMaxSignalDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options import SecurityMonitoringRuleNewValueOptions
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_forget_after import (
    SecurityMonitoringRuleNewValueOptionsForgetAfter,
)
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_learning_duration import (
    SecurityMonitoringRuleNewValueOptionsLearningDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_learning_method import (
    SecurityMonitoringRuleNewValueOptionsLearningMethod,
)
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_learning_threshold import (
    SecurityMonitoringRuleNewValueOptionsLearningThreshold,
)
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_query import SecurityMonitoringRuleQuery
from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
    SecurityMonitoringRuleQueryAggregation,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_update_payload import SecurityMonitoringRuleUpdatePayload

body = SecurityMonitoringRuleUpdatePayload(
    cases=[
        SecurityMonitoringRuleCase(
            notifications=[],
            status=SecurityMonitoringRuleSeverity("critical"),
        ),
    ],
    filters=[
        SecurityMonitoringFilter(
            action=SecurityMonitoringFilterAction("require"),
        ),
    ],
    has_extended_title=True,
    options=SecurityMonitoringRuleOptions(
        decrease_criticality_based_on_env=False,
        detection_method=SecurityMonitoringRuleDetectionMethod("threshold"),
        evaluation_window=SecurityMonitoringRuleEvaluationWindow(0),
        hardcoded_evaluator_type=SecurityMonitoringRuleHardcodedEvaluatorType("log4shell"),
        impossible_travel_options=SecurityMonitoringRuleImpossibleTravelOptions(
            baseline_user_locations=True,
        ),
        keep_alive=SecurityMonitoringRuleKeepAlive(0),
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration(0),
        new_value_options=SecurityMonitoringRuleNewValueOptions(
            forget_after=SecurityMonitoringRuleNewValueOptionsForgetAfter(1),
            learning_duration=SecurityMonitoringRuleNewValueOptionsLearningDuration(0),
            learning_method=SecurityMonitoringRuleNewValueOptionsLearningMethod("duration"),
            learning_threshold=SecurityMonitoringRuleNewValueOptionsLearningThreshold(0),
        ),
    ),
    queries=[
        SecurityMonitoringRuleQuery(
            aggregation=SecurityMonitoringRuleQueryAggregation("count"),
            distinct_fields=[],
            group_by_fields=[],
            metrics=[],
        ),
    ],
    tags=[],
    version=1,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_rule(rule_id="rule_id", body=body)

    print(response)
