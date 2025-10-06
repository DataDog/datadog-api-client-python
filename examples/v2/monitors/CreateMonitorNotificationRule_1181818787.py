"""
Create a monitor notification rule with conditional recipients returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_condition import MonitorNotificationRuleCondition
from datadog_api_client.v2.model.monitor_notification_rule_conditional_recipients import (
    MonitorNotificationRuleConditionalRecipients,
)
from datadog_api_client.v2.model.monitor_notification_rule_create_request import MonitorNotificationRuleCreateRequest
from datadog_api_client.v2.model.monitor_notification_rule_create_request_data import (
    MonitorNotificationRuleCreateRequestData,
)
from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType

body = MonitorNotificationRuleCreateRequest(
    data=MonitorNotificationRuleCreateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterTags(
                tags=[
                    "test:example-monitor",
                ],
            ),
            name="test rule",
            conditional_recipients=MonitorNotificationRuleConditionalRecipients(
                conditions=[
                    MonitorNotificationRuleCondition(
                        scope="transition_type:is_alert",
                        recipients=[
                            "slack-test-channel",
                            "jira-test",
                        ],
                    ),
                ],
            ),
        ),
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_notification_rule(body=body)

    print(response)
