"""
Create a detection rule with detection method 'third_party' returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_rule_detection_method import SecurityMonitoringRuleDetectionMethod
from datadog_api_client.v2.model.security_monitoring_rule_keep_alive import SecurityMonitoringRuleKeepAlive
from datadog_api_client.v2.model.security_monitoring_rule_max_signal_duration import (
    SecurityMonitoringRuleMaxSignalDuration,
)
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_third_party_options import (
    SecurityMonitoringRuleThirdPartyOptions,
)
from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate
from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
    SecurityMonitoringStandardRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_third_party_root_query import SecurityMonitoringThirdPartyRootQuery
from datadog_api_client.v2.model.security_monitoring_third_party_rule_case_create import (
    SecurityMonitoringThirdPartyRuleCaseCreate,
)

body = SecurityMonitoringStandardRuleCreatePayload(
    name="Example-Security-Monitoring",
    type=SecurityMonitoringRuleTypeCreate.LOG_DETECTION,
    is_enabled=True,
    third_party_cases=[
        SecurityMonitoringThirdPartyRuleCaseCreate(
            query="status:error",
            name="high",
            status=SecurityMonitoringRuleSeverity.HIGH,
        ),
        SecurityMonitoringThirdPartyRuleCaseCreate(
            query="status:info",
            name="low",
            status=SecurityMonitoringRuleSeverity.LOW,
        ),
    ],
    queries=[],
    cases=[],
    message="This is a third party rule",
    options=SecurityMonitoringRuleOptions(
        detection_method=SecurityMonitoringRuleDetectionMethod.THIRD_PARTY,
        keep_alive=SecurityMonitoringRuleKeepAlive.ZERO_MINUTES,
        max_signal_duration=SecurityMonitoringRuleMaxSignalDuration.ZERO_MINUTES,
        third_party_rule_options=SecurityMonitoringRuleThirdPartyOptions(
            default_status=SecurityMonitoringRuleSeverity.INFO,
            root_queries=[
                SecurityMonitoringThirdPartyRootQuery(
                    query="source:guardduty @details.alertType:*EC2*",
                    group_by_fields=[
                        "instance-id",
                    ],
                ),
                SecurityMonitoringThirdPartyRootQuery(
                    query="source:guardduty",
                    group_by_fields=[],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_rule(body=body)

    print(response)
