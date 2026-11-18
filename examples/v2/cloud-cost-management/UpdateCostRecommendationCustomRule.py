"""
Update a cost recommendation custom rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter import CostRecommendationCustomRuleFilter
from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter_type import (
    CostRecommendationCustomRuleFilterType,
)
from datadog_api_client.v2.model.cost_recommendation_custom_rule_settings import CostRecommendationCustomRuleSettings
from datadog_api_client.v2.model.cost_recommendation_custom_rule_type import CostRecommendationCustomRuleType
from datadog_api_client.v2.model.cost_recommendation_custom_rule_update_attributes import (
    CostRecommendationCustomRuleUpdateAttributes,
)
from datadog_api_client.v2.model.cost_recommendation_custom_rule_update_data import (
    CostRecommendationCustomRuleUpdateData,
)
from datadog_api_client.v2.model.cost_recommendation_custom_rule_update_request import (
    CostRecommendationCustomRuleUpdateRequest,
)

body = CostRecommendationCustomRuleUpdateRequest(
    data=CostRecommendationCustomRuleUpdateData(
        attributes=CostRecommendationCustomRuleUpdateAttributes(
            enabled=False,
            filters=[
                CostRecommendationCustomRuleFilter(
                    filter_type=CostRecommendationCustomRuleFilterType.IS,
                    tag="env",
                    values=[
                        "staging",
                    ],
                ),
            ],
            name="Staging and development instances",
            notes="Staging instances can run with less headroom.",
            settings=CostRecommendationCustomRuleSettings(
                lookback_days=14.0,
                max_cpu_user_limit=0.05,
            ),
        ),
        id="8a1b6f3e-2c4d-4e5f-9a7b-1c2d3e4f5a6b",
        type=CostRecommendationCustomRuleType.CUSTOM_RULES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_cost_recommendation_custom_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_cost_recommendation_custom_rule(custom_rule_id="custom_rule_id", body=body)

    print(response)
