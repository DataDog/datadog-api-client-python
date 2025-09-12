"""
Reorder rulesets returns "Successfully reordered rulesets" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.reorder_ruleset_resource_array import ReorderRulesetResourceArray
from datadog_api_client.v2.model.reorder_ruleset_resource_data import ReorderRulesetResourceData
from datadog_api_client.v2.model.reorder_ruleset_resource_data_type import ReorderRulesetResourceDataType

body = ReorderRulesetResourceArray(
    data=[
        ReorderRulesetResourceData(
            type=ReorderRulesetResourceDataType.RULESET,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.reorder_rulesets(body=body)
