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
    from datadog_api_client.v2.model.ai_gateway_policy_tier_request import AiGatewayPolicyTierRequest


class AiGatewayPolicyRequestAttributes(ModelNormal):
    validations = {
        "inbound": {
            "max_length": 256,
            "min_length": 1,
        },
        "tiers": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_policy_tier_request import AiGatewayPolicyTierRequest

        return {
            "inbound": (str,),
            "priority": (int,),
            "tiers": ([AiGatewayPolicyTierRequest],),
        }

    attribute_map = {
        "inbound": "inbound",
        "priority": "priority",
        "tiers": "tiers",
    }

    def __init__(
        self_, inbound: str, tiers: List[AiGatewayPolicyTierRequest], priority: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Attributes used to create or replace a routing policy document.

        :param inbound: Inbound request pattern.
        :type inbound: str

        :param priority: Routing priority.
        :type priority: int, optional

        :param tiers:
        :type tiers: [AiGatewayPolicyTierRequest]
        """
        if priority is not unset:
            kwargs["priority"] = priority
        super().__init__(kwargs)

        self_.inbound = inbound
        self_.tiers = tiers
