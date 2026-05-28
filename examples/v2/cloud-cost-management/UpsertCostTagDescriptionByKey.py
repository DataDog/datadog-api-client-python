"""
Upsert a Cloud Cost Management tag description returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.cost_tag_description_type import CostTagDescriptionType
from datadog_api_client.v2.model.cost_tag_description_upsert_request import CostTagDescriptionUpsertRequest
from datadog_api_client.v2.model.cost_tag_description_upsert_request_data import CostTagDescriptionUpsertRequestData
from datadog_api_client.v2.model.cost_tag_description_upsert_request_data_attributes import (
    CostTagDescriptionUpsertRequestDataAttributes,
)

body = CostTagDescriptionUpsertRequest(
    data=CostTagDescriptionUpsertRequestData(
        attributes=CostTagDescriptionUpsertRequestDataAttributes(
            cloud="aws",
            description="AWS account that owns this cost.",
        ),
        id="account_id",
        type=CostTagDescriptionType.COST_TAG_DESCRIPTION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.upsert_cost_tag_description_by_key(tag_key="tag_key", body=body)
