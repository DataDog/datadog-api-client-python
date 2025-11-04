"""
Create connection returns "Connection created successfully" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.create_connection_request import CreateConnectionRequest
from datadog_api_client.v2.model.create_connection_request_data import CreateConnectionRequestData
from datadog_api_client.v2.model.create_connection_request_data_attributes import CreateConnectionRequestDataAttributes
from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
    CreateConnectionRequestDataAttributesFieldsItems,
)
from datadog_api_client.v2.model.update_connection_request_data_type import UpdateConnectionRequestDataType

body = CreateConnectionRequest(
    data=CreateConnectionRequestData(
        attributes=CreateConnectionRequestDataAttributes(
            fields=[
                CreateConnectionRequestDataAttributesFieldsItems(
                    description="Customer subscription tier from `CRM`",
                    display_name="Customer Tier",
                    id="customer_tier",
                    source_name="subscription_tier",
                    type="string",
                ),
                CreateConnectionRequestDataAttributesFieldsItems(
                    description="Customer lifetime value in `USD`",
                    display_name="Lifetime Value",
                    id="lifetime_value",
                    source_name="ltv",
                    type="number",
                ),
            ],
            join_attribute="user_email",
            join_type="email",
            type="ref_table",
        ),
        id="crm-integration",
        type=UpdateConnectionRequestDataType.CONNECTION_ID,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    api_instance.create_connection(entity="users", body=body)
