"""
Patch a signal-based notification rule returns "Notification rule successfully patched." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType
from datadog_api_client.v2.model.patch_notification_rule_parameters import PatchNotificationRuleParameters
from datadog_api_client.v2.model.patch_notification_rule_parameters_data import PatchNotificationRuleParametersData
from datadog_api_client.v2.model.patch_notification_rule_parameters_data_attributes import (
    PatchNotificationRuleParametersDataAttributes,
)
from datadog_api_client.v2.model.rule_severity import RuleSeverity
from datadog_api_client.v2.model.rule_types_items import RuleTypesItems
from datadog_api_client.v2.model.selectors import Selectors
from datadog_api_client.v2.model.trigger_source import TriggerSource

# there is a valid "valid_signal_notification_rule" in the system
VALID_SIGNAL_NOTIFICATION_RULE_DATA_ID = environ["VALID_SIGNAL_NOTIFICATION_RULE_DATA_ID"]

body = PatchNotificationRuleParameters(
    data=PatchNotificationRuleParametersData(
        attributes=PatchNotificationRuleParametersDataAttributes(
            enabled=True,
            name="Rule 1",
            selectors=Selectors(
                query="(source:production_service OR env:prod)",
                rule_types=[
                    RuleTypesItems.MISCONFIGURATION,
                    RuleTypesItems.ATTACK_PATH,
                ],
                severities=[
                    RuleSeverity.CRITICAL,
                ],
                trigger_source=TriggerSource.SECURITY_FINDINGS,
            ),
            targets=[
                "@john.doe@email.com",
            ],
            time_aggregation=86400,
            version=1,
        ),
        id=VALID_SIGNAL_NOTIFICATION_RULE_DATA_ID,
        type=NotificationRulesType.NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.patch_signal_notification_rule(id=VALID_SIGNAL_NOTIFICATION_RULE_DATA_ID, body=body)

    print(response)
