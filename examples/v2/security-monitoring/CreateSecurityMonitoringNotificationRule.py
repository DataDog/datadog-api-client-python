"""
Create a notification rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_notification_rule_create_attributes import (
    SecurityMonitoringNotificationRuleCreateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_create_data import (
    SecurityMonitoringNotificationRuleCreateData,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_create_request import (
    SecurityMonitoringNotificationRuleCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_selectors import (
    SecurityMonitoringNotificationRuleSelectors,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
    SecurityMonitoringNotificationRuleType,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_types import SecurityMonitoringRuleTypes

body = SecurityMonitoringNotificationRuleCreateRequest(
    data=SecurityMonitoringNotificationRuleCreateData(
        attributes=SecurityMonitoringNotificationRuleCreateAttributes(
            enabled=True,
            name="Example-Security-Monitoring",
            selectors=SecurityMonitoringNotificationRuleSelectors(
                attributes=[
                    "test:123",
                    "env:prod",
                ],
                implicit_vm_rule_match=False,
                rule_tags=[
                    "test:123",
                ],
                rule_types=[
                    SecurityMonitoringRuleTypes.APPLICATION_SECURITY,
                    SecurityMonitoringRuleTypes.LOG_DETECTION,
                ],
                severities=[
                    SecurityMonitoringRuleSeverity.HIGH,
                ],
                signal_tags=[
                    "env:prod",
                ],
            ),
            targets=[
                "@slack-test",
            ],
        ),
        type=SecurityMonitoringNotificationRuleType.NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_monitoring_notification_rule(body=body)

    print(response)
