"""
Create an On-Call notification rule for a user returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.create_on_call_notification_rule_request import CreateOnCallNotificationRuleRequest
from datadog_api_client.v2.model.create_on_call_notification_rule_request_data import (
    CreateOnCallNotificationRuleRequestData,
)
from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType
from datadog_api_client.v2.model.on_call_notification_rule_category import OnCallNotificationRuleCategory
from datadog_api_client.v2.model.on_call_notification_rule_channel_relationship import (
    OnCallNotificationRuleChannelRelationship,
)
from datadog_api_client.v2.model.on_call_notification_rule_channel_relationship_data import (
    OnCallNotificationRuleChannelRelationshipData,
)
from datadog_api_client.v2.model.on_call_notification_rule_relationships import OnCallNotificationRuleRelationships
from datadog_api_client.v2.model.on_call_notification_rule_request_attributes import (
    OnCallNotificationRuleRequestAttributes,
)
from datadog_api_client.v2.model.on_call_notification_rule_type import OnCallNotificationRuleType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "oncall_email_notification_channel" in the system
ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID = environ["ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID"]

body = CreateOnCallNotificationRuleRequest(
    data=CreateOnCallNotificationRuleRequestData(
        attributes=OnCallNotificationRuleRequestAttributes(
            category=OnCallNotificationRuleCategory.HIGH_URGENCY,
            delay_minutes=0,
        ),
        relationships=OnCallNotificationRuleRelationships(
            channel=OnCallNotificationRuleChannelRelationship(
                data=OnCallNotificationRuleChannelRelationshipData(
                    id=ONCALL_EMAIL_NOTIFICATION_CHANNEL_DATA_ID,
                    type=NotificationChannelType.NOTIFICATION_CHANNELS,
                ),
            ),
        ),
        type=OnCallNotificationRuleType.NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_user_notification_rule(user_id=USER_DATA_ID, body=body)

    print(response)
