"""
Update Custom Costs file returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.custom_costs_file_update_attributes import CustomCostsFileUpdateAttributes
from datadog_api_client.v2.model.custom_costs_file_update_data import CustomCostsFileUpdateData
from datadog_api_client.v2.model.custom_costs_file_update_request import CustomCostsFileUpdateRequest
from datadog_api_client.v2.model.custom_costs_file_update_type import CustomCostsFileUpdateType

# there is a valid "custom_costs_file" in the system
CUSTOM_COSTS_FILE_DATA_ID = environ["CUSTOM_COSTS_FILE_DATA_ID"]

body = CustomCostsFileUpdateRequest(
    data=CustomCostsFileUpdateData(
        attributes=CustomCostsFileUpdateAttributes(
            ai_provider=True,
        ),
        id=CUSTOM_COSTS_FILE_DATA_ID,
        type=CustomCostsFileUpdateType.COST_METADATA,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_custom_costs_file(file_id=CUSTOM_COSTS_FILE_DATA_ID, body=body)

    print(response)
