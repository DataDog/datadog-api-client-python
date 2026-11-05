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
    from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes import (
        AiGatewayCaptureDeleteRequestDataAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_type import (
        AiGatewayCaptureDeleteRequestDataType,
    )


class AiGatewayCaptureDeleteRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_attributes import (
            AiGatewayCaptureDeleteRequestDataAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data_type import (
            AiGatewayCaptureDeleteRequestDataType,
        )

        return {
            "attributes": (AiGatewayCaptureDeleteRequestDataAttributes,),
            "id": (UUID,),
            "type": (AiGatewayCaptureDeleteRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayCaptureDeleteRequestDataAttributes,
        id: UUID,
        type: AiGatewayCaptureDeleteRequestDataType,
        **kwargs,
    ):
        """
        Override identifier, revisions, and confirmation required for deletion.

        :param attributes: Revisions and confirmation used to delete the override.
        :type attributes: AiGatewayCaptureDeleteRequestDataAttributes

        :param id: UUID of the override to delete. Must match the ``id`` path parameter.
        :type id: UUID

        :param type: Data capture overrides resource type.
        :type type: AiGatewayCaptureDeleteRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
