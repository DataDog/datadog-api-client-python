"""
Replace an AI Gateway data capture override returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_capture_scope import AiGatewayCaptureScope
from datadog_api_client.v2.model.ai_gateway_capture_update_request import AiGatewayCaptureUpdateRequest
from datadog_api_client.v2.model.ai_gateway_capture_update_request_data import AiGatewayCaptureUpdateRequestData
from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_attributes import (
    AiGatewayCaptureUpdateRequestDataAttributes,
)
from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_attributes_mode import (
    AiGatewayCaptureUpdateRequestDataAttributesMode,
)
from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_attributes_operation import (
    AiGatewayCaptureUpdateRequestDataAttributesOperation,
)
from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_type import (
    AiGatewayCaptureUpdateRequestDataType,
)
from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
from uuid import UUID

body = AiGatewayCaptureUpdateRequest(
    data=AiGatewayCaptureUpdateRequestData(
        attributes=AiGatewayCaptureUpdateRequestDataAttributes(
            configuration_revision="capture-revision-1",
            metadata_capture=[
                AiGatewayMetadataCaptureItem.TOOL_USAGE,
                AiGatewayMetadataCaptureItem.TOOL_OUTPUT_SIZE,
                AiGatewayMetadataCaptureItem.TOOL_NAMES,
            ],
            mode=AiGatewayCaptureUpdateRequestDataAttributesMode.METADATA_ONLY,
            name="Research",
            operation=AiGatewayCaptureUpdateRequestDataAttributesOperation.CREATE,
            revision=1,
            scope=AiGatewayCaptureScope(
                tags=dict(
                    env="prod",
                ),
            ),
        ),
        id=UUID("11111111-1111-4111-8111-111111111111"),
        type=AiGatewayCaptureUpdateRequestDataType.DATA_CAPTURE_OVERRIDES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_data_capture_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_data_capture_override(
        id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
