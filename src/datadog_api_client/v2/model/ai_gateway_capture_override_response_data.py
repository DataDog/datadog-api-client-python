# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_capture_override_response_data_attributes import (
        AiGatewayCaptureOverrideResponseDataAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_override_response_data_type import (
        AiGatewayCaptureOverrideResponseDataType,
    )


class AiGatewayCaptureOverrideResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_override_response_data_attributes import (
            AiGatewayCaptureOverrideResponseDataAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_override_response_data_type import (
            AiGatewayCaptureOverrideResponseDataType,
        )

        return {
            "attributes": (AiGatewayCaptureOverrideResponseDataAttributes,),
            "id": (UUID,),
            "type": (AiGatewayCaptureOverrideResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayCaptureOverrideResponseDataAttributes,
        id: UUID,
        type: AiGatewayCaptureOverrideResponseDataType,
        **kwargs,
    ):
        """
        Saved data capture override with its identifier, mode, scope, and revision.

        :param attributes: Saved name, capture mode, request filters, and revision of the override.
        :type attributes: AiGatewayCaptureOverrideResponseDataAttributes

        :param id: UUID of the saved override, used to retrieve it from the configuration or change it.
        :type id: UUID

        :param type: Data capture overrides resource type.
        :type type: AiGatewayCaptureOverrideResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
