# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_reasoning_control import AiGatewayModelReasoningControl


class AiGatewayModelReasoning(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_reasoning_control import AiGatewayModelReasoningControl

        return {
            "controls": ([AiGatewayModelReasoningControl],),
        }

    attribute_map = {
        "controls": "controls",
    }

    def __init__(self_, controls: List[AiGatewayModelReasoningControl], **kwargs):
        """
        Supported reasoning controls. Absence means controls are unknown or unavailable.

        :param controls:
        :type controls: [AiGatewayModelReasoningControl]
        """
        super().__init__(kwargs)

        self_.controls = controls
