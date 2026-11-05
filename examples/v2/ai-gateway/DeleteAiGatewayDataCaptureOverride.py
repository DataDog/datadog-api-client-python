"""
Delete an AI Gateway data capture override returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_capture_delete_request import AiGatewayCaptureDeleteRequest
from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data import AiGatewayCaptureDeleteRequestData
from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes import (
    AiGatewayCaptureDeleteRequestDataAttributes,
)
from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes_mode import (
    AiGatewayCaptureDeleteRequestDataAttributesMode,
)
from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes_operation import (
    AiGatewayCaptureDeleteRequestDataAttributesOperation,
)
from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_type import (
    AiGatewayCaptureDeleteRequestDataType,
)
from datadog_api_client.v2.model.ai_gateway_capture_scope import AiGatewayCaptureScope
from uuid import UUID

body = AiGatewayCaptureDeleteRequest(
    data=AiGatewayCaptureDeleteRequestData(
        attributes=AiGatewayCaptureDeleteRequestDataAttributes(
            configuration_revision="capture-revision-1",
            mode=AiGatewayCaptureDeleteRequestDataAttributesMode.METADATA_ONLY,
            name="Research",
            operation=AiGatewayCaptureDeleteRequestDataAttributesOperation.CREATE,
            revision=1,
            scope=AiGatewayCaptureScope(
                tags=dict(
                    env="prod",
                ),
            ),
        ),
        id=UUID("11111111-1111-4111-8111-111111111111"),
        type=AiGatewayCaptureDeleteRequestDataType.DATA_CAPTURE_OVERRIDES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_ai_gateway_data_capture_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    api_instance.delete_ai_gateway_data_capture_override(id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)
