"""
Create a RUM operation strong link returns "Created" response
"""

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

body = RUMOperationStrongLinkCreateRequest(
    data=RUMOperationStrongLinkCreateRequestData(
        attributes=RUMOperationStrongLinkCreateRequestAttributes(
            description=None,
            feature_id="feature-123",
            operation_id="abc12345-1234-5678-abcd-ef1234567890",
            status=RUMOperationStrongLinkStatus.CONFIRMED,
            tags=[],
        ),
        type=RUMOperationStrongLinkType.STRONG_LINKS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_rum_operation_strong_link"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.create_rum_operation_strong_link(body=body)

    print(response)
