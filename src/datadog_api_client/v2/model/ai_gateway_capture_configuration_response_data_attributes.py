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
    from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
    from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data_attributes_default_mode import (
        AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_override import AiGatewayCaptureOverride


class AiGatewayCaptureConfigurationResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_metadata_capture_item import AiGatewayMetadataCaptureItem
        from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data_attributes_default_mode import (
            AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_override import AiGatewayCaptureOverride

        return {
            "configuration_revision": (str,),
            "default_metadata_capture": ([AiGatewayMetadataCaptureItem],),
            "default_mode": (AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode,),
            "overrides": ([AiGatewayCaptureOverride],),
        }

    attribute_map = {
        "configuration_revision": "configuration_revision",
        "default_metadata_capture": "default_metadata_capture",
        "default_mode": "default_mode",
        "overrides": "overrides",
    }

    def __init__(
        self_,
        configuration_revision: str,
        default_mode: AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode,
        overrides: List[AiGatewayCaptureOverride],
        default_metadata_capture: Union[List[AiGatewayMetadataCaptureItem], UnsetType] = unset,
        **kwargs,
    ):
        """
        Organization default mode, scoped overrides, and current configuration revision.

        :param configuration_revision: Opaque revision of the organization default and all overrides. Writes require the revision returned by a current read or preview.
        :type configuration_revision: str

        :param default_metadata_capture: Items Metadata-only capture adds, each listed once. An item requires the items whose information it already reveals: ``tool_output_size`` , ``tool_names`` and ``conversation_shape`` require ``tool_usage`` , and ``input_size_by_role`` requires ``tool_output_size``. A set that leaves out a required item is rejected. When several Metadata-only overrides match a request, it gets only the items all of them select.
        :type default_metadata_capture: [AiGatewayMetadataCaptureItem], optional

        :param default_mode: Default capture mode for the organization. Change it in **Org defaults**.
        :type default_mode: AiGatewayCaptureConfigurationResponseDataAttributesDefaultMode

        :param overrides: Scoped overrides currently configured for the organization.
        :type overrides: [AiGatewayCaptureOverride]
        """
        if default_metadata_capture is not unset:
            kwargs["default_metadata_capture"] = default_metadata_capture
        super().__init__(kwargs)

        self_.configuration_revision = configuration_revision
        self_.default_mode = default_mode
        self_.overrides = overrides
