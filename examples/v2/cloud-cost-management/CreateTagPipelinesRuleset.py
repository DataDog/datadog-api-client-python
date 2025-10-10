"""
Create tag pipeline ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.create_ruleset_request import CreateRulesetRequest
from datadog_api_client.v2.model.create_ruleset_request_data import CreateRulesetRequestData
from datadog_api_client.v2.model.create_ruleset_request_data_attributes import CreateRulesetRequestDataAttributes
from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items import (
    CreateRulesetRequestDataAttributesRulesItems,
)
from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query import (
    CreateRulesetRequestDataAttributesRulesItemsQuery,
)
from datadog_api_client.v2.model.create_ruleset_request_data_attributes_rules_items_query_addition import (
    CreateRulesetRequestDataAttributesRulesItemsQueryAddition,
)
from datadog_api_client.v2.model.create_ruleset_request_data_type import CreateRulesetRequestDataType

body = CreateRulesetRequest(
    data=CreateRulesetRequestData(
        attributes=CreateRulesetRequestDataAttributes(
            enabled=True,
            rules=[
                CreateRulesetRequestDataAttributesRulesItems(
                    enabled=True,
                    mapping=None,
                    name="Add Cost Center Tag",
                    query=CreateRulesetRequestDataAttributesRulesItemsQuery(
                        addition=CreateRulesetRequestDataAttributesRulesItemsQueryAddition(
                            key="cost_center",
                            value="engineering",
                        ),
                        case_insensitivity=False,
                        if_not_exists=True,
                        query='account_id:"123456789" AND service:"web-api"',
                    ),
                    reference_table=None,
                ),
            ],
        ),
        id="New Ruleset",
        type=CreateRulesetRequestDataType.CREATE_RULESET,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_tag_pipelines_ruleset(body=body)

    print(response)
