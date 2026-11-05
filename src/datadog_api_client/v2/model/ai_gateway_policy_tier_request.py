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
    from datadog_api_client.v2.model.ai_gateway_policy_target_request import AiGatewayPolicyTargetRequest


class AiGatewayPolicyTierRequest(ModelNormal):
    validations = {
        "targets": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_policy_target_request import AiGatewayPolicyTargetRequest

        return {
            "priority": (int,),
            "targets": ([AiGatewayPolicyTargetRequest],),
        }

    attribute_map = {
        "priority": "priority",
        "targets": "targets",
    }

    def __init__(self_, targets: List[AiGatewayPolicyTargetRequest], priority: Union[int, UnsetType] = unset, **kwargs):
        """
        Routing policy tier supplied in a request.

        :param priority: Routing priority.
        :type priority: int, optional

        :param targets:
        :type targets: [AiGatewayPolicyTargetRequest]
        """
        if priority is not unset:
            kwargs["priority"] = priority
        super().__init__(kwargs)

        self_.targets = targets
