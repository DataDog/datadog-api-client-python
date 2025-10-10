"""
Update custom allocation rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.arbitrary_cost_upsert_request import ArbitraryCostUpsertRequest
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data import ArbitraryCostUpsertRequestData
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes import (
    ArbitraryCostUpsertRequestDataAttributes,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_costs_to_allocate_items import (
    ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy import (
    ArbitraryCostUpsertRequestDataAttributesStrategy,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy_based_on_costs_items import (
    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems,
)
from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_type import ArbitraryCostUpsertRequestDataType

body = ArbitraryCostUpsertRequest(
    data=ArbitraryCostUpsertRequestData(
        attributes=ArbitraryCostUpsertRequestDataAttributes(
            costs_to_allocate=[
                ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems(
                    condition="is",
                    tag="account_id",
                    value="123456789",
                    values=[],
                ),
                ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems(
                    condition="in",
                    tag="environment",
                    value="",
                    values=[
                        "production",
                        "staging",
                    ],
                ),
            ],
            enabled=True,
            order_id=1,
            provider=[
                "aws",
                "gcp",
            ],
            rule_name="example-arbitrary-cost-rule",
            strategy=ArbitraryCostUpsertRequestDataAttributesStrategy(
                allocated_by_tag_keys=[
                    "team",
                    "environment",
                ],
                based_on_costs=[
                    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems(
                        condition="is",
                        tag="service",
                        value="web-api",
                        values=[],
                    ),
                    ArbitraryCostUpsertRequestDataAttributesStrategyBasedOnCostsItems(
                        condition="not in",
                        tag="team",
                        value="",
                        values=[
                            "legacy",
                            "deprecated",
                        ],
                    ),
                ],
                granularity="daily",
                method="proportional",
            ),
            type="shared",
        ),
        type=ArbitraryCostUpsertRequestDataType.UPSERT_ARBITRARY_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_custom_allocation_rule(rule_id=683, body=body)

    print(response)
