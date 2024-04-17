"""
Update a notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_notification_rule_selectors import (
    SecurityMonitoringNotificationRuleSelectors,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_type import (
    SecurityMonitoringNotificationRuleType,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_update_attributes import (
    SecurityMonitoringNotificationRuleUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_update_data import (
    SecurityMonitoringNotificationRuleUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_notification_rule_update_request import (
    SecurityMonitoringNotificationRuleUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_types import SecurityMonitoringRuleTypes

# there is a valid "notification_rule" in the system
NOTIFICATION_RULE_DATA_ID = environ["NOTIFICATION_RULE_DATA_ID"]

body = SecurityMonitoringNotificationRuleUpdateRequest(
    data=SecurityMonitoringNotificationRuleUpdateData(
        attributes=SecurityMonitoringNotificationRuleUpdateAttributes(
            version=1,
            name="Example-Security-Monitoring",
            enabled=False,
            selectors=SecurityMonitoringNotificationRuleSelectors(
                attributes=[
                    "fim:true",
                ],
                implicit_vm_rule_match=False,
                rule_tags=[
                    "fim:true",
                ],
                severities=[
                    SecurityMonitoringRuleSeverity.HIGH,
                ],
                signal_tags=[],
                rule_types=[
                    SecurityMonitoringRuleTypes.LOG_DETECTION,
                    SecurityMonitoringRuleTypes.CLOUD_CONFIGURATION,
                ],
            ),
            targets=[
                "test2",
            ],
        ),
        type=SecurityMonitoringNotificationRuleType.NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.edit_security_monitoring_notification_rule(
        notification_rule_id=NOTIFICATION_RULE_DATA_ID, body=body
    )

    print(response)
