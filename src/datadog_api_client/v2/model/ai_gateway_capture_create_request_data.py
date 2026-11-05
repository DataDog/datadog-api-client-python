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
    from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes import (
        AiGatewayCaptureCreateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_type import (
        AiGatewayCaptureCreateRequestDataType,
    )


class AiGatewayCaptureCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_attributes import (
            AiGatewayCaptureCreateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_create_request_data_type import (
            AiGatewayCaptureCreateRequestDataType,
        )

        return {
            "attributes": (AiGatewayCaptureCreateRequestDataAttributes,),
            "id": (UUID,),
            "type": (AiGatewayCaptureCreateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayCaptureCreateRequestDataAttributes,
        id: UUID,
        type: AiGatewayCaptureCreateRequestDataType,
        **kwargs,
    ):
        """
        New data capture override with a client-generated UUID and its settings.

        :param attributes: Settings and configuration revision for creating the override.
        :type attributes: AiGatewayCaptureCreateRequestDataAttributes

        :param id: Client-generated UUID for the override.
        :type id: UUID

        :param type: Data capture overrides resource type.
        :type type: AiGatewayCaptureCreateRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
