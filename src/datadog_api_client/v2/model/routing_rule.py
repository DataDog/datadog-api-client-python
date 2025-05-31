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
    from datadog_api_client.v2.model.routing_rule_attributes import RoutingRuleAttributes
    from datadog_api_client.v2.model.routing_rule_relationships import RoutingRuleRelationships
    from datadog_api_client.v2.model.routing_rule_type import RoutingRuleType


class RoutingRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.routing_rule_attributes import RoutingRuleAttributes
        from datadog_api_client.v2.model.routing_rule_relationships import RoutingRuleRelationships
        from datadog_api_client.v2.model.routing_rule_type import RoutingRuleType

        return {
            "attributes": (RoutingRuleAttributes,),
            "id": (str,),
            "relationships": (RoutingRuleRelationships,),
            "type": (RoutingRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: RoutingRuleType,
        attributes: Union[RoutingRuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[RoutingRuleRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a routing rule, including its attributes, relationships, and unique identifier.

        :param attributes: Defines the configurable attributes of a routing rule, such as actions, query, time restriction, and urgency.
        :type attributes: RoutingRuleAttributes, optional

        :param id: Specifies the unique identifier of this routing rule.
        :type id: str, optional

        :param relationships: Specifies relationships for a routing rule, linking to associated policy resources.
        :type relationships: RoutingRuleRelationships, optional

        :param type: Team routing rules resource type.
        :type type: RoutingRuleType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
