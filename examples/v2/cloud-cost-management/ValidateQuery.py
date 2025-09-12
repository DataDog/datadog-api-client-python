"""
Validate query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.rules_validate_query_request import RulesValidateQueryRequest
from datadog_api_client.v2.model.rules_validate_query_request_data import RulesValidateQueryRequestData
from datadog_api_client.v2.model.rules_validate_query_request_data_attributes import (
    RulesValidateQueryRequestDataAttributes,
)
from datadog_api_client.v2.model.rules_validate_query_request_data_type import RulesValidateQueryRequestDataType

body = RulesValidateQueryRequest(
    data=RulesValidateQueryRequestData(
        attributes=RulesValidateQueryRequestDataAttributes(
            query="example:query AND test:true",
        ),
        type=RulesValidateQueryRequestDataType.VALIDATE_QUERY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.validate_query(body=body)

    print(response)
