"""
Create a detection rule with detection method "third_party" returns "OK" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
from datadog_api_client.v2.model.security_monitoring_rule_create_payload import SecurityMonitoringRuleCreatePayload
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
from datadog_api_client.v2.model.security_monitoring_rule_query_create import SecurityMonitoringRuleQueryCreate
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_third_party_options import (
    SecurityMonitoringRuleThirdPartyOptions,
)

body = SecurityMonitoringRuleCreatePayload(
    name="Example-Create_a_detection_rule_with_detection_method_third_party_returns_OK_response",
    queries=[
        SecurityMonitoringRuleQueryCreate(
            query="@test:true",
            aggregation=SecurityMonitoringRuleQueryAggregation("none"),
            group_by_fields=[],
            distinct_fields=[],
        )
    ],
    filters=[],
    cases=[SecurityMonitoringRuleCaseCreate(name="", status=SecurityMonitoringRuleSeverity("info"), notifications=[])],
    options=SecurityMonitoringRuleOptions(
        detection_method=SecurityMonitoringRuleDetectionMethod("third_party"),
        evaluation_window=SecurityMonitoringRuleEvaluationWindow(0),
        keep_alive=SecurityMonitoringRuleKeepAlive(3600),
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration(86400),
        third_party_rule_options=SecurityMonitoringRuleThirdPartyOptions(
            root_query="@pop", default_status=SecurityMonitoringRuleSeverity("low")
        ),
    ),
    message="Example-Create_a_detection_rule_with_detection_method_third_party_returns_OK_response message",
    tags=[],
    is_enabled=True,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
