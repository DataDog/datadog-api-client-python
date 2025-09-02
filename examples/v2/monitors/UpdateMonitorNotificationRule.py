"""
Update a monitor notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType
from datadog_api_client.v2.model.monitor_notification_rule_update_request import MonitorNotificationRuleUpdateRequest
from datadog_api_client.v2.model.monitor_notification_rule_update_request_data import (
    MonitorNotificationRuleUpdateRequestData,
)

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = environ["MONITOR_NOTIFICATION_RULE_DATA_ID"]

body = MonitorNotificationRuleUpdateRequest(
    data=MonitorNotificationRuleUpdateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterTags(
                tags=[
                    "test:example-monitor",
                    "host:abc",
                ],
            ),
            name="updated rule",
            recipients=[
                "slack-test-channel",
            ],
        ),
        id=MONITOR_NOTIFICATION_RULE_DATA_ID,
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_notification_rule(rule_id=MONITOR_NOTIFICATION_RULE_DATA_ID, body=body)

    print(response)
