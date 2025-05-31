# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.routing_rule_relationships_policy import RoutingRuleRelationshipsPolicy


class RoutingRuleRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.routing_rule_relationships_policy import RoutingRuleRelationshipsPolicy

        return {
            "policy": (RoutingRuleRelationshipsPolicy,),
        }

    attribute_map = {
        "policy": "policy",
    }

    def __init__(self_, policy: Union[RoutingRuleRelationshipsPolicy, UnsetType] = unset, **kwargs):
        """
        Specifies relationships for a routing rule, linking to associated policy resources.

        :param policy: Defines the relationship that links a routing rule to a policy.
        :type policy: RoutingRuleRelationshipsPolicy, optional
        """
        if policy is not unset:
            kwargs["policy"] = policy
        super().__init__(kwargs)
