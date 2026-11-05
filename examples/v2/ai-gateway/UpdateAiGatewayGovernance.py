"""
Replace AI Gateway governance controls returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_data_capture_mode import AiGatewayDataCaptureMode
from datadog_api_client.v2.model.ai_gateway_governance_replace_attributes import AiGatewayGovernanceReplaceAttributes
from datadog_api_client.v2.model.ai_gateway_governance_replace_data import AiGatewayGovernanceReplaceData
from datadog_api_client.v2.model.ai_gateway_governance_replace_request import AiGatewayGovernanceReplaceRequest
from datadog_api_client.v2.model.ai_gateway_governance_type import AiGatewayGovernanceType
from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
from datadog_api_client.v2.model.ai_gateway_zdr_mode import AiGatewayZDRMode

body = AiGatewayGovernanceReplaceRequest(
    data=AiGatewayGovernanceReplaceData(
        attributes=AiGatewayGovernanceReplaceAttributes(
            data_capture_mode=AiGatewayDataCaptureMode.METADATA_ONLY,
            metadata_capture=[
                AiGatewayMetadataCaptureItem.TOOL_USAGE,
                AiGatewayMetadataCaptureItem.TOOL_OUTPUT_SIZE,
                AiGatewayMetadataCaptureItem.TOOL_NAMES,
            ],
            zdr_mode=AiGatewayZDRMode.OFF,
        ),
        id="organization",
        type=AiGatewayGovernanceType.GOVERNANCE,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_governance"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_governance(body=body)

    print(response)
