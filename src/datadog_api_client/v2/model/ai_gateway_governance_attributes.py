# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_data_capture_mode import AiGatewayDataCaptureMode
    from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
    from datadog_api_client.v2.model.ai_gateway_zdr_mode import AiGatewayZDRMode


class AiGatewayGovernanceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_data_capture_mode import AiGatewayDataCaptureMode
        from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
        from datadog_api_client.v2.model.ai_gateway_zdr_mode import AiGatewayZDRMode

        return {
            "data_capture_mode": (AiGatewayDataCaptureMode,),
            "metadata_capture": ([AiGatewayMetadataCaptureItem],),
            "zdr_mode": (AiGatewayZDRMode,),
        }

    attribute_map = {
        "data_capture_mode": "data_capture_mode",
        "metadata_capture": "metadata_capture",
        "zdr_mode": "zdr_mode",
    }

    def __init__(
        self_,
        data_capture_mode: AiGatewayDataCaptureMode,
        zdr_mode: AiGatewayZDRMode,
        metadata_capture: Union[List[AiGatewayMetadataCaptureItem], UnsetType] = unset,
        **kwargs,
    ):
        """
        Organization-wide AI Gateway governance controls.

        :param data_capture_mode: Controls whether AI Gateway captures request and response content in addition to metadata.
        :type data_capture_mode: AiGatewayDataCaptureMode

        :param metadata_capture: Items Metadata-only capture adds, each listed once. An item requires the items whose information it already reveals: ``tool_output_size`` , ``tool_names`` and ``conversation_shape`` require ``tool_usage`` , and ``input_size_by_role`` requires ``tool_output_size``. A set that leaves out a required item is rejected. When several Metadata-only overrides match a request, it gets only the items all of them select.
        :type metadata_capture: [AiGatewayMetadataCaptureItem], optional

        :param zdr_mode: Zero data retention requirement for the organization's requests.
        :type zdr_mode: AiGatewayZDRMode
        """
        if metadata_capture is not unset:
            kwargs["metadata_capture"] = metadata_capture
        super().__init__(kwargs)

        self_.data_capture_mode = data_capture_mode
        self_.zdr_mode = zdr_mode
