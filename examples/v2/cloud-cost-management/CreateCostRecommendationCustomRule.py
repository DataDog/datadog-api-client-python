"""
Create a cost recommendation custom rule returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.cost_recommendation_custom_rule_create_attributes import (
    CostRecommendationCustomRuleCreateAttributes,
)
from datadog_api_client.v2.model.cost_recommendation_custom_rule_create_data import (
    CostRecommendationCustomRuleCreateData,
)
from datadog_api_client.v2.model.cost_recommendation_custom_rule_create_request import (
    CostRecommendationCustomRuleCreateRequest,
)
from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter import CostRecommendationCustomRuleFilter
from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter_type import (
    CostRecommendationCustomRuleFilterType,
)
from datadog_api_client.v2.model.cost_recommendation_custom_rule_settings import CostRecommendationCustomRuleSettings
from datadog_api_client.v2.model.cost_recommendation_custom_rule_type import CostRecommendationCustomRuleType

body = CostRecommendationCustomRuleCreateRequest(
    data=CostRecommendationCustomRuleCreateData(
        attributes=CostRecommendationCustomRuleCreateAttributes(
            enabled=True,
            filters=[
                CostRecommendationCustomRuleFilter(
                    filter_type=CostRecommendationCustomRuleFilterType.IS,
                    tag="env",
                    values=[
                        "staging",
                    ],
                ),
            ],
            name="Staging instances",
            notes="Staging instances can run with less headroom.",
            recommender_id="aws_ec2_instance_unused",
            settings=CostRecommendationCustomRuleSettings(
                lookback_days=14.0,
                max_cpu_user_limit=0.05,
            ),
        ),
        type=CostRecommendationCustomRuleType.CUSTOM_RULES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_cost_recommendation_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_cost_recommendation_custom_rule(body=body)

    print(response)
