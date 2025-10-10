"""
Reorder custom allocation rules returns "Successfully reordered rules" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.reorder_rule_resource_array import ReorderRuleResourceArray
from datadog_api_client.v2.model.reorder_rule_resource_data import ReorderRuleResourceData
from datadog_api_client.v2.model.reorder_rule_resource_data_type import ReorderRuleResourceDataType

body = ReorderRuleResourceArray(
    data=[
        ReorderRuleResourceData(
            id="456",
            type=ReorderRuleResourceDataType.ARBITRARY_RULE,
        ),
        ReorderRuleResourceData(
            id="123",
            type=ReorderRuleResourceDataType.ARBITRARY_RULE,
        ),
        ReorderRuleResourceData(
            id="789",
            type=ReorderRuleResourceDataType.ARBITRARY_RULE,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.reorder_custom_allocation_rules(body=body)
