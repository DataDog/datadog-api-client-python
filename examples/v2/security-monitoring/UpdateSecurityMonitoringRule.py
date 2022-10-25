"""
Update an existing rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
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
from datadog_api_client.v2.model.security_monitoring_rule_update_payload import SecurityMonitoringRuleUpdatePayload
from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery

# there is a valid "security_rule" in the system
SECURITY_RULE_ID = environ["SECURITY_RULE_ID"]

body = SecurityMonitoringRuleUpdatePayload(
    name="Example-Update_an_existing_rule_returns_OK_response-Updated",
    queries=[
        SecurityMonitoringStandardRuleQuery(
            query="@test:true",
            aggregation=SecurityMonitoringRuleQueryAggregation.COUNT,
            group_by_fields=[],
            distinct_fields=[],
            metrics=[],
        ),
    ],
    filters=[],
    cases=[
        SecurityMonitoringRuleCase(
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
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_rule(rule_id=SECURITY_RULE_ID, body=body)

    print(response)
