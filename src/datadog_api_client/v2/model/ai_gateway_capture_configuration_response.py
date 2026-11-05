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
    from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data import (
        AiGatewayCaptureConfigurationResponseData,
    )


class AiGatewayCaptureConfigurationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_configuration_response_data import (
            AiGatewayCaptureConfigurationResponseData,
        )

        return {
            "data": (AiGatewayCaptureConfigurationResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiGatewayCaptureConfigurationResponseData, **kwargs):
        """
        Response containing the organization data capture configuration.

        :param data: Organization data capture configuration, including its default mode and scoped overrides.
        :type data: AiGatewayCaptureConfigurationResponseData
        """
        super().__init__(kwargs)

        self_.data = data
