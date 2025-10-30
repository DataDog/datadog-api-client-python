"""
Update connection returns "Connection updated successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
    CreateConnectionRequestDataAttributesFieldsItems,
)
from datadog_api_client.v2.model.update_connection_request import UpdateConnectionRequest
from datadog_api_client.v2.model.update_connection_request_data import UpdateConnectionRequestData
from datadog_api_client.v2.model.update_connection_request_data_attributes import UpdateConnectionRequestDataAttributes
from datadog_api_client.v2.model.update_connection_request_data_attributes_fields_to_update_items import (
    UpdateConnectionRequestDataAttributesFieldsToUpdateItems,
)
from datadog_api_client.v2.model.update_connection_request_data_type import UpdateConnectionRequestDataType

body = UpdateConnectionRequest(
    data=UpdateConnectionRequestData(
        attributes=UpdateConnectionRequestDataAttributes(
            fields_to_add=[
                CreateConnectionRequestDataAttributesFieldsItems(
                    description="Net Promoter Score from customer surveys",
                    display_name="NPS Score",
                    groups=[
                        "Satisfaction",
                        "Metrics",
                    ],
                    id="nps_score",
                    source_name="net_promoter_score",
                    type="number",
                ),
            ],
            fields_to_delete=[
                "old_revenue_field",
            ],
            fields_to_update=[
                UpdateConnectionRequestDataAttributesFieldsToUpdateItems(
                    field_id="lifetime_value",
                    updated_display_name="Customer Lifetime Value (`USD`)",
                    updated_groups=[
                        "Financial",
                        "Metrics",
                    ],
                ),
            ],
        ),
        id="crm-integration",
        type=UpdateConnectionRequestDataType.CONNECTION_ID,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    api_instance.update_connection(entity="users", body=body)
