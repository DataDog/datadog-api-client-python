"""
Create a RUM operation link returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi
from datadog_api_client.v2.model.rum_operation_strong_link_create_request import RUMOperationStrongLinkCreateRequest
from datadog_api_client.v2.model.rum_operation_strong_link_create_request_attributes import (
    RUMOperationStrongLinkCreateRequestAttributes,
)
from datadog_api_client.v2.model.rum_operation_strong_link_create_request_data import (
    RUMOperationStrongLinkCreateRequestData,
)
from datadog_api_client.v2.model.rum_operation_strong_link_status import RUMOperationStrongLinkStatus
from datadog_api_client.v2.model.rum_operation_strong_link_type import RUMOperationStrongLinkType

# there is a valid "rum_operation" in the system
RUM_OPERATION_DATA_ID = environ["RUM_OPERATION_DATA_ID"]

body = RUMOperationStrongLinkCreateRequest(
    data=RUMOperationStrongLinkCreateRequestData(
        type=RUMOperationStrongLinkType.STRONG_LINKS,
        attributes=RUMOperationStrongLinkCreateRequestAttributes(
            operation_id=RUM_OPERATION_DATA_ID,
            feature_id="bdd-examplerumoperation",
            status=RUMOperationStrongLinkStatus.DRAFT,
            tags=[
                "team:rum-backend",
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.create_rum_operation_strong_link(body=body)

    print(response)
