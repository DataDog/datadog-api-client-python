"""
Validate a detection rule with detection method 'new_value' with enabled feature 'instantaneousBaseline' returns "OK"
response
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
from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
    SecurityMonitoringRuleQueryAggregation,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate
from datadog_api_client.v2.model.security_monitoring_standard_data_source import SecurityMonitoringStandardDataSource
from datadog_api_client.v2.model.security_monitoring_standard_rule_payload import SecurityMonitoringStandardRulePayload
from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery

body = SecurityMonitoringStandardRulePayload(
    cases=[
        SecurityMonitoringRuleCaseCreate(
            name="",
            status=SecurityMonitoringRuleSeverity.INFO,
            notifications=[],
        ),
    ],
    has_extended_title=True,
    is_enabled=True,
    message="My security monitoring rule",
    name="My security monitoring rule",
    options=SecurityMonitoringRuleOptions(
        evaluation_window=SecurityMonitoringRuleEvaluationWindow.ZERO_MINUTES,
        keep_alive=SecurityMonitoringRuleKeepAlive.FIVE_MINUTES,
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.TEN_MINUTES,
        detection_method=SecurityMonitoringRuleDetectionMethod.NEW_VALUE,
        new_value_options=SecurityMonitoringRuleNewValueOptions(
            forget_after=SecurityMonitoringRuleNewValueOptionsForgetAfter.ONE_WEEK,
            instantaneous_baseline=True,
            learning_duration=SecurityMonitoringRuleNewValueOptionsLearningDuration.ONE_DAY,
            learning_threshold=SecurityMonitoringRuleNewValueOptionsLearningThreshold.ZERO_OCCURRENCES,
            learning_method=SecurityMonitoringRuleNewValueOptionsLearningMethod.DURATION,
        ),
    ),
    queries=[
        SecurityMonitoringStandardRuleQuery(
            query="source:source_here",
            group_by_fields=[
                "@userIdentity.assumed_role",
            ],
            distinct_fields=[],
            metric="name",
            metrics=[
                "name",
            ],
            aggregation=SecurityMonitoringRuleQueryAggregation.NEW_VALUE,
            name="",
            data_source=SecurityMonitoringStandardDataSource.LOGS,
        ),
    ],
    tags=[
        "env:prod",
        "team:security",
    ],
    type=SecurityMonitoringRuleTypeCreate.LOG_DETECTION,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.validate_security_monitoring_rule(body=body)
