"""
Send AI tool user activity returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.ai_impact_user_activity_attributes import AIImpactUserActivityAttributes
from datadog_api_client.v2.model.ai_impact_user_activity_data import AIImpactUserActivityData
from datadog_api_client.v2.model.ai_impact_user_activity_request import AIImpactUserActivityRequest
from datadog_api_client.v2.model.ai_impact_user_activity_type import AIImpactUserActivityType

body = AIImpactUserActivityRequest(
    data=[
        AIImpactUserActivityData(
            attributes=AIImpactUserActivityAttributes(
                day="2026-05-26",
                is_active=True,
                models=[
                    "claude-sonnet-4.5",
                    "gpt-5",
                ],
                tools=[
                    "Claude Code",
                    "Cursor",
                ],
                user_email="user@example.com",
            ),
            type=AIImpactUserActivityType.AI_IMPACT_USER_ACTIVITY,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    api_instance.create_ai_impact_user_activity(body=body)
