"""
Create or replace a budget's custom forecast returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.custom_forecast_entry import CustomForecastEntry
from datadog_api_client.v2.model.custom_forecast_entry_tag_filter import CustomForecastEntryTagFilter
from datadog_api_client.v2.model.custom_forecast_type import CustomForecastType
from datadog_api_client.v2.model.custom_forecast_upsert_request import CustomForecastUpsertRequest
from datadog_api_client.v2.model.custom_forecast_upsert_request_data import CustomForecastUpsertRequestData
from datadog_api_client.v2.model.custom_forecast_upsert_request_data_attributes import (
    CustomForecastUpsertRequestDataAttributes,
)

body = CustomForecastUpsertRequest(
    data=CustomForecastUpsertRequestData(
        attributes=CustomForecastUpsertRequestDataAttributes(
            budget_uid="00000000-0000-0000-0000-000000000001",
            entries=[
                CustomForecastEntry(
                    amount=400.0,
                    month=202501,
                    tag_filters=[
                        CustomForecastEntryTagFilter(
                            tag_key="service",
                            tag_value="ec2",
                        ),
                    ],
                ),
            ],
        ),
        id="",
        type=CustomForecastType.CUSTOM_FORECAST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_custom_forecast"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.upsert_custom_forecast(body=body)

    print(response)
