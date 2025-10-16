"""
Create a scheduled detection rule returns "OK" response
"""

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
from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate
from datadog_api_client.v2.model.security_monitoring_scheduling_options import SecurityMonitoringSchedulingOptions
from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
    SecurityMonitoringStandardRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery

body = SecurityMonitoringStandardRuleCreatePayload(
    name="Example-Security-Monitoring",
    queries=[
        SecurityMonitoringStandardRuleQuery(
            query="@test:true",
            aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
            group_by_fields=[],
            distinct_fields=[],
            indexes=[
                "main",
            ],
        ),
    ],
    filters=[],
    cases=[
        SecurityMonitoringRuleCaseCreate(
            name="",
            status=SecurityMonitoringRuleSeverity.INFO,
            condition="a > 0",
            notifications=[],
        ),
    ],
    options=SecurityMonitoringRuleOptions(
        evaluation_window=SecurityMonitoringRuleEvaluationWindow.FIFTEEN_MINUTES,
        keep_alive=SecurityMonitoringRuleKeepAlive.ONE_HOUR,
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ONE_DAY,
    ),
    message="Test rule",
    tags=[],
    is_enabled=True,
    type=SecurityMonitoringRuleTypeCreate.LOG_DETECTION,
    scheduling_options=SecurityMonitoringSchedulingOptions(
        rrule="FREQ=HOURLY;INTERVAL=2;",
        start="2025-06-18T12:00:00",
        timezone="Europe/Paris",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
