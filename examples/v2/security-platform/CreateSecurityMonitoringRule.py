"""
Create a detection rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_platform_api import SecurityPlatformApi
from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
from datadog_api_client.v2.model.security_monitoring_filter_action import SecurityMonitoringFilterAction
from datadog_api_client.v2.model.security_monitoring_rule_create_payload import SecurityMonitoringRuleCreatePayload
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
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate

body = SecurityMonitoringRuleCreatePayload(
    cases=[],
    filters=[
        SecurityMonitoringFilter(
            action=SecurityMonitoringFilterAction("require"),
        ),
    ],
    has_extended_title=True,
    is_enabled=True,
    message="",
    name="My security monitoring rule.",
    options=SecurityMonitoringRuleOptions(
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
        ),
    ),
    queries=[],
    tags=[
        "env:prod",
        "team:security",
    ],
    type=SecurityMonitoringRuleTypeCreate("log_detection"),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityPlatformApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
