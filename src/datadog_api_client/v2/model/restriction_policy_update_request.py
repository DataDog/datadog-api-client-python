# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.restriction_policy_binding import RestrictionPolicyBinding
from datadog_api_client.v2.model.restriction_policy_binding import RestrictionPolicyBinding

if TYPE_CHECKING:
    from datadog_api_client.v2.model.restriction_policy import RestrictionPolicy


@dataclass
class RestrictionPolicyUpdateRequestJSON:
    id: str
    bindings: Union[List[RestrictionPolicyBinding], UnsetType] = unset


class RestrictionPolicyUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.restriction_policy import RestrictionPolicy

        return {
            "data": (RestrictionPolicy,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = RestrictionPolicyUpdateRequestJSON

    def __init__(self_, data: RestrictionPolicy, **kwargs):
        """
        Update request for a restriction policy.

        :param data: Restriction policy object.
        :type data: RestrictionPolicy
        """
        super().__init__(kwargs)

        self_.data = data
