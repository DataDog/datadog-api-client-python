"""
Create an AI Gateway data capture override returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_capture_create_request import AiGatewayCaptureCreateRequest
from datadog_api_client.v2.model.ai_gateway_capture_create_request_data import AiGatewayCaptureCreateRequestData
from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes import (
    AiGatewayCaptureCreateRequestDataAttributes,
)
from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes_mode import (
    AiGatewayCaptureCreateRequestDataAttributesMode,
)
from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes_operation import (
    AiGatewayCaptureCreateRequestDataAttributesOperation,
)
from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_type import (
    AiGatewayCaptureCreateRequestDataType,
)
from datadog_api_client.v2.model.ai_gateway_capture_scope import AiGatewayCaptureScope
from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
from uuid import UUID

body = AiGatewayCaptureCreateRequest(
    data=AiGatewayCaptureCreateRequestData(
        attributes=AiGatewayCaptureCreateRequestDataAttributes(
            configuration_revision="capture-revision-1",
            metadata_capture=[
                AiGatewayMetadataCaptureItem.TOOL_USAGE,
                AiGatewayMetadataCaptureItem.TOOL_OUTPUT_SIZE,
                AiGatewayMetadataCaptureItem.TOOL_NAMES,
            ],
            mode=AiGatewayCaptureCreateRequestDataAttributesMode.METADATA_ONLY,
            name="Research",
            operation=AiGatewayCaptureCreateRequestDataAttributesOperation.CREATE,
            revision=1,
            scope=AiGatewayCaptureScope(
                tags=dict(
                    env="prod",
                ),
            ),
        ),
        id=UUID("11111111-1111-4111-8111-111111111111"),
        type=AiGatewayCaptureCreateRequestDataType.DATA_CAPTURE_OVERRIDES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_ai_gateway_data_capture_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.create_ai_gateway_data_capture_override(body=body)

    print(response)
