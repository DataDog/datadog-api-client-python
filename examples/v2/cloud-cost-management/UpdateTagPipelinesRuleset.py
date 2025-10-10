"""
Update tag pipeline ruleset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.update_ruleset_request import UpdateRulesetRequest
from datadog_api_client.v2.model.update_ruleset_request_data import UpdateRulesetRequestData
from datadog_api_client.v2.model.update_ruleset_request_data_attributes import UpdateRulesetRequestDataAttributes
from datadog_api_client.v2.model.update_ruleset_request_data_attributes_rules_items import (
    UpdateRulesetRequestDataAttributesRulesItems,
)
from datadog_api_client.v2.model.update_ruleset_request_data_attributes_rules_items_mapping import (
    UpdateRulesetRequestDataAttributesRulesItemsMapping,
)
from datadog_api_client.v2.model.update_ruleset_request_data_type import UpdateRulesetRequestDataType

body = UpdateRulesetRequest(
    data=UpdateRulesetRequestData(
        attributes=UpdateRulesetRequestDataAttributes(
            enabled=True,
            last_version=3611102,
            rules=[
                UpdateRulesetRequestDataAttributesRulesItems(
                    enabled=True,
                    mapping=UpdateRulesetRequestDataAttributesRulesItemsMapping(
                        destination_key="team_owner",
                        if_not_exists=True,
                        source_keys=[
                            "account_name",
                            "account_id",
                        ],
                    ),
                    name="Account Name Mapping",
                    query=None,
                    reference_table=None,
                ),
            ],
        ),
        id="New Ruleset",
        type=UpdateRulesetRequestDataType.UPDATE_RULESET,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_tag_pipelines_ruleset(ruleset_id="ee10c3ff-312f-464c-b4f6-46adaa6d00a1", body=body)

    print(response)
