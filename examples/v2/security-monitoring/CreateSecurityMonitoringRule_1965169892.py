"""
Create a detection rule with type 'application_security 'returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_case_action import SecurityMonitoringRuleCaseAction
from datadog_api_client.v2.model.security_monitoring_rule_case_action_options import (
    SecurityMonitoringRuleCaseActionOptions,
)
from datadog_api_client.v2.model.security_monitoring_rule_case_action_type import SecurityMonitoringRuleCaseActionType
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
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate
from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
    SecurityMonitoringStandardRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery

body = SecurityMonitoringStandardRuleCreatePayload(
    type=SecurityMonitoringRuleTypeCreate.APPLICATION_SECURITY,
    name="Example-Security-Monitoring_appsec_rule",
    queries=[
        SecurityMonitoringStandardRuleQuery(
            query="@appsec.security_activity:business_logic.users.login.failure",
            aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
            group_by_fields=[
                "service",
                "@http.client_ip",
            ],
            distinct_fields=[],
        ),
    ],
    filters=[],
    cases=[
        SecurityMonitoringRuleCaseCreate(
            name="",
            status=SecurityMonitoringRuleSeverity.INFO,
            notifications=[],
            condition="a > 100000",
            actions=[
                SecurityMonitoringRuleCaseAction(
                    type=SecurityMonitoringRuleCaseActionType.BLOCK_IP,
                    options=SecurityMonitoringRuleCaseActionOptions(
                        duration=900,
                    ),
                ),
                SecurityMonitoringRuleCaseAction(
                    type=SecurityMonitoringRuleCaseActionType.USER_BEHAVIOR,
                    options=SecurityMonitoringRuleCaseActionOptions(
                        user_behavior_name="behavior",
                    ),
                ),
            ],
        ),
    ],
    options=SecurityMonitoringRuleOptions(
        keep_alive=SecurityMonitoringRuleKeepAlive.ONE_HOUR,
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ONE_DAY,
        evaluation_window=SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES,
        detection_method=SecurityMonitoringRuleDetectionMethod.THRESHOLD,
    ),
    is_enabled=True,
    message="Test rule",
    tags=[],
    group_signals_by=[
        "service",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
