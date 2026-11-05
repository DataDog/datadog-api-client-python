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
    from datadog_api_client.v2.model.ai_gateway_policy_target import AiGatewayPolicyTarget


class AiGatewayPolicyTier(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_policy_target import AiGatewayPolicyTarget

        return {
            "targets": ([AiGatewayPolicyTarget],),
        }

    attribute_map = {
        "targets": "targets",
    }

    def __init__(self_, targets: List[AiGatewayPolicyTarget], **kwargs):
        """
        Resolved routing policy tier.

        :param targets:
        :type targets: [AiGatewayPolicyTarget]
        """
        super().__init__(kwargs)

        self_.targets = targets
