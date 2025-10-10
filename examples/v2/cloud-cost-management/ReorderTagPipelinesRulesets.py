"""
Reorder tag pipeline rulesets returns "Successfully reordered rulesets" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.reorder_ruleset_resource_array import ReorderRulesetResourceArray
from datadog_api_client.v2.model.reorder_ruleset_resource_data import ReorderRulesetResourceData
from datadog_api_client.v2.model.reorder_ruleset_resource_data_type import ReorderRulesetResourceDataType

body = ReorderRulesetResourceArray(
    data=[
        ReorderRulesetResourceData(
            id="55ef2385-9ae1-4410-90c4-5ac1b60fec10",
            type=ReorderRulesetResourceDataType.RULESET,
        ),
        ReorderRulesetResourceData(
            id="a7b8c9d0-1234-5678-9abc-def012345678",
            type=ReorderRulesetResourceDataType.RULESET,
        ),
        ReorderRulesetResourceData(
            id="f1e2d3c4-b5a6-9780-1234-567890abcdef",
            type=ReorderRulesetResourceDataType.RULESET,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.reorder_tag_pipelines_rulesets(body=body)
