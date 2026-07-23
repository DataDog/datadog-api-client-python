"""
Update a RUM operation strong link returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi
from datadog_api_client.v2.model.rum_operation_strong_link_type import RUMOperationStrongLinkType
from datadog_api_client.v2.model.rum_operation_strong_link_update_request import RUMOperationStrongLinkUpdateRequest
from datadog_api_client.v2.model.rum_operation_strong_link_update_request_attributes import (
    RUMOperationStrongLinkUpdateRequestAttributes,
)
from datadog_api_client.v2.model.rum_operation_strong_link_update_request_data import (
    RUMOperationStrongLinkUpdateRequestData,
)
from datadog_api_client.v2.model.rum_operation_strong_link_update_status import RUMOperationStrongLinkUpdateStatus

body = RUMOperationStrongLinkUpdateRequest(
    data=RUMOperationStrongLinkUpdateRequestData(
        attributes=RUMOperationStrongLinkUpdateRequestAttributes(
            status=RUMOperationStrongLinkUpdateStatus.CONFIRMED,
        ),
        type=RUMOperationStrongLinkType.STRONG_LINKS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_rum_operation_strong_link"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.update_rum_operation_strong_link(
        operation_id="operation_id", feature_id="feature_id", body=body
    )

    print(response)
