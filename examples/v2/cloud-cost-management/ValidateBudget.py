"""
Validate budget returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.budget_validation_request import BudgetValidationRequest
from datadog_api_client.v2.model.budget_validation_request_data import BudgetValidationRequestData
from datadog_api_client.v2.model.budget_with_entries_data_attributes import BudgetWithEntriesDataAttributes
from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items import (
    BudgetWithEntriesDataAttributesEntriesItems,
)
from datadog_api_client.v2.model.budget_with_entries_data_attributes_entries_items_tag_filters_items import (
    BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems,
)
from datadog_api_client.v2.model.budget_with_entries_data_type import BudgetWithEntriesDataType

body = BudgetValidationRequest(
    data=BudgetValidationRequestData(
        attributes=BudgetWithEntriesDataAttributes(
            created_at=1738258683590,
            created_by="00000000-0a0a-0a0a-aaa0-00000000000a",
            end_month=202502,
            entries=[
                BudgetWithEntriesDataAttributesEntriesItems(
                    amount=500.0,
                    month=202501,
                    tag_filters=[
                        BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems(
                            tag_key="service",
                            tag_value="ec2",
                        ),
                    ],
                ),
                BudgetWithEntriesDataAttributesEntriesItems(
                    amount=500.0,
                    month=202502,
                    tag_filters=[
                        BudgetWithEntriesDataAttributesEntriesItemsTagFiltersItems(
                            tag_key="service",
                            tag_value="ec2",
                        ),
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
        id="1",
        type=BudgetWithEntriesDataType.BUDGET,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.validate_budget(body=body)

    print(response)
