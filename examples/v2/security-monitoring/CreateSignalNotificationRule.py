"""
Create a new signal-based notification rule returns "Successfully created the notification rule." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.create_notification_rule_parameters import CreateNotificationRuleParameters
from datadog_api_client.v2.model.create_notification_rule_parameters_data import CreateNotificationRuleParametersData
from datadog_api_client.v2.model.create_notification_rule_parameters_data_attributes import (
    CreateNotificationRuleParametersDataAttributes,
)
from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType
from datadog_api_client.v2.model.rule_severity import RuleSeverity
from datadog_api_client.v2.model.rule_types_items import RuleTypesItems
from datadog_api_client.v2.model.selectors import Selectors
from datadog_api_client.v2.model.trigger_source import TriggerSource

body = CreateNotificationRuleParameters(
    data=CreateNotificationRuleParametersData(
        attributes=CreateNotificationRuleParametersDataAttributes(
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
        ),
        type=NotificationRulesType.NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_signal_notification_rule(body=body)

    print(response)
