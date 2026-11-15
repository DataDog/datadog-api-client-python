"""
Update a cost recommendation notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.cost_recommendation_notification_rule_destination_type import (
    CostRecommendationNotificationRuleDestinationType,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_frequency import (
    CostRecommendationNotificationRuleFrequency,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_action import (
    CostRecommendationNotificationRuleMessageAction,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_actions import (
    CostRecommendationNotificationRuleMessageActions,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization import (
    CostRecommendationNotificationRuleMessageCustomization,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_header import (
    CostRecommendationNotificationRuleMessageCustomizationHeader,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_mode import (
    CostRecommendationNotificationRuleMessageCustomizationMode,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization_per_rec import (
    CostRecommendationNotificationRuleMessageCustomizationPerRec,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_type import (
    CostRecommendationNotificationRuleType,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_update_attributes import (
    CostRecommendationNotificationRuleUpdateAttributes,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_update_data import (
    CostRecommendationNotificationRuleUpdateData,
)
from datadog_api_client.v2.model.cost_recommendation_notification_rule_update_request import (
    CostRecommendationNotificationRuleUpdateRequest,
)

body = CostRecommendationNotificationRuleUpdateRequest(
    data=CostRecommendationNotificationRuleUpdateData(
        attributes=CostRecommendationNotificationRuleUpdateAttributes(
            channel_id="C0456ABCD",
            destination_type=CostRecommendationNotificationRuleDestinationType.SLACK,
            enabled=False,
            frequency=CostRecommendationNotificationRuleFrequency.WEEKLY,
            interval_execution_date="2026-11-02",
            interval_execution_time="09:30",
            mention_targets=[
                "U01ABCDE",
            ],
            message_customization=CostRecommendationNotificationRuleMessageCustomization(
                actions=CostRecommendationNotificationRuleMessageActions(
                    view_in_ccm=CostRecommendationNotificationRuleMessageAction(
                        bulk=True,
                        per_rec=True,
                    ),
                ),
                header=CostRecommendationNotificationRuleMessageCustomizationHeader(
                    custom_text=" recommendations to review this week.",
                    notification_name=True,
                    total_savings=True,
                ),
                include_tags=[
                    "team",
                ],
                mode=CostRecommendationNotificationRuleMessageCustomizationMode.STRUCTURED,
                per_rec=CostRecommendationNotificationRuleMessageCustomizationPerRec(
                    effort=True,
                    risk=True,
                    why=True,
                ),
            ),
            name="Production recommendations",
            scope_query="service:api AND env:prod",
            timezone="America/New_York",
            weekly_execution_day="monday",
            weekly_execution_time="09:30",
            workspace_id="T0123ABCD",
        ),
        id="2c59b248-6a91-4f95-972a-dc236cae9cbb",
        type=CostRecommendationNotificationRuleType.NOTIFICATION_RULES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_cost_recommendation_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_recommendation_notification_rule(
        notification_rule_id="notification_rule_id", body=body
    )

    print(response)
