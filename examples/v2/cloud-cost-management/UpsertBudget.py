"""
Create or update a budget returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.budget_attributes import BudgetAttributes
from datadog_api_client.v2.model.budget_with_entries import BudgetWithEntries
from datadog_api_client.v2.model.budget_with_entries_data import BudgetWithEntriesData
from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items import (
    BudgetWithEntriesDataAttributesEntriesItems,
)
from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items_tag_filters_items import (
    BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems,
)

body = BudgetWithEntries(
    data=BudgetWithEntriesData(
        attributes=BudgetAttributes(
            created_at=1738258683590,
            created_by="00000000-0a0a-0a0a-aaa0-00000000000a",
            end_month=202502,
            entries=[
                BudgetWithEntriesDataAttributesEntriesItems(
                    tag_filters=[
                        BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems(),
                    ],
                ),
            ],
            metrics_query="aws.cost.amortized{service:ec2} by {service}",
            name="my budget",
            org_id=123,
            start_month=202501,
            total_amount=1000.0,
            updated_at=1738258683590,
            updated_by="00000000-0a0a-0a0a-aaa0-00000000000a",
        ),
        id="00000000-0a0a-0a0a-aaa0-00000000000a",
        type="",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.upsert_budget(body=body)

    print(response)
