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
    from datadog_api_client.v2.model.ai_gateway_policy_request_attributes import AiGatewayPolicyRequestAttributes
    from datadog_api_client.v2.model.ai_gateway_policy_type import AiGatewayPolicyType


class AiGatewayPolicyRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_policy_request_attributes import AiGatewayPolicyRequestAttributes
        from datadog_api_client.v2.model.ai_gateway_policy_type import AiGatewayPolicyType

        return {
            "attributes": (AiGatewayPolicyRequestAttributes,),
            "type": (AiGatewayPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayPolicyRequestAttributes, type: AiGatewayPolicyType, **kwargs):
        """
        Data used to create or replace a routing policy document.

        :param attributes: Attributes used to create or replace a routing policy document.
        :type attributes: AiGatewayPolicyRequestAttributes

        :param type: AI Gateway routing policy resource type.
        :type type: AiGatewayPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
