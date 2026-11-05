# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data_attributes import (
        AiGatewayCaptureConfigurationResponseDataAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data_type import (
        AiGatewayCaptureConfigurationResponseDataType,
    )


class AiGatewayCaptureConfigurationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data_attributes import (
            AiGatewayCaptureConfigurationResponseDataAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data_type import (
            AiGatewayCaptureConfigurationResponseDataType,
        )

        return {
            "attributes": (AiGatewayCaptureConfigurationResponseDataAttributes,),
            "id": (str,),
            "type": (AiGatewayCaptureConfigurationResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayCaptureConfigurationResponseDataAttributes,
        id: str,
        type: AiGatewayCaptureConfigurationResponseDataType,
        **kwargs,
    ):
        """
        Organization data capture configuration, including its default mode and scoped overrides.

        :param attributes: Organization default mode, scoped overrides, and current configuration revision.
        :type attributes: AiGatewayCaptureConfigurationResponseDataAttributes

        :param id: Identifier of the organization configuration resource, always ``organization``.
        :type id: str

        :param type: Data capture configurations resource type.
        :type type: AiGatewayCaptureConfigurationResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
