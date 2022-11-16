"""
Create a detection rule with type 'impossible_travel' returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
from datadog_api_client.v2.model.security_monitoring_rule_detection_method import SecurityMonitoringRuleDetectionMethod
from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
    SecurityMonitoringRuleEvaluationWindow,
)
from datadog_api_client.v2.model.security_monitoring_rule_impossible_travel_options import (
    SecurityMonitoringRuleImpossibleTravelOptions,
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
    queries=[
        SecurityMonitoringStandardRuleQuery(
            aggregation=SecurityMonitoringRuleQueryAggregation.GEO_DATA,
            group_by_fields=[
                "@usr.id",
            ],
            distinct_fields=[],
            metric="@network.client.geoip",
            query="*",
        ),
    ],
    cases=[
        SecurityMonitoringRuleCaseCreate(
            name="",
            status=SecurityMonitoringRuleSeverity.INFO,
            notifications=[],
        ),
    ],
    has_extended_title=True,
    message="test",
    is_enabled=True,
    options=SecurityMonitoringRuleOptions(
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ONE_DAY,
        evaluation_window=SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES,
        keep_alive=SecurityMonitoringRuleKeepAlive.ONE_HOUR,
        detection_method=SecurityMonitoringRuleDetectionMethod.IMPOSSIBLE_TRAVEL,
        impossible_travel_options=SecurityMonitoringRuleImpossibleTravelOptions(
            baseline_user_locations=False,
        ),
    ),
    name="Example-Create_a_detection_rule_with_type_impossible_travel_returns_OK_response",
    type=SecurityMonitoringRuleTypeCreate.LOG_DETECTION,
    tags=[],
    filters=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
