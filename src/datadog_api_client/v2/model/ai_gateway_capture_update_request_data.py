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
    from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_attributes import (
        AiGatewayCaptureUpdateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_type import (
        AiGatewayCaptureUpdateRequestDataType,
    )


class AiGatewayCaptureUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_attributes import (
            AiGatewayCaptureUpdateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_update_request_data_type import (
            AiGatewayCaptureUpdateRequestDataType,
        )

        return {
            "attributes": (AiGatewayCaptureUpdateRequestDataAttributes,),
            "id": (UUID,),
            "type": (AiGatewayCaptureUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayCaptureUpdateRequestDataAttributes,
        id: UUID,
        type: AiGatewayCaptureUpdateRequestDataType,
        **kwargs,
    ):
        """
        Existing override identifier, replacement settings, and revisions required for the update.

        :param attributes: Replacement settings and revisions for updating the override.
        :type attributes: AiGatewayCaptureUpdateRequestDataAttributes

        :param id: UUID of the override to replace. Must match the ``id`` path parameter.
        :type id: UUID

        :param type: Data capture overrides resource type.
        :type type: AiGatewayCaptureUpdateRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
