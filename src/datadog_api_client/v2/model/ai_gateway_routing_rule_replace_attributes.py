# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_request import AiGatewayRoutingRuleTierRequest


class AiGatewayRoutingRuleReplaceAttributes(ModelNormal):
    validations = {
        "tiers": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_request import AiGatewayRoutingRuleTierRequest

        return {
            "description": (str, none_type),
            "display_name": (str, none_type),
            "expected_updated_at": (datetime,),
            "removed_target_ids": ([int],),
            "tiers": ([AiGatewayRoutingRuleTierRequest],),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "expected_updated_at": "expected_updated_at",
        "removed_target_ids": "removed_target_ids",
        "tiers": "tiers",
    }

    def __init__(
        self_,
        description: Union[str, none_type, UnsetType] = unset,
        display_name: Union[str, none_type, UnsetType] = unset,
        expected_updated_at: Union[datetime, UnsetType] = unset,
        removed_target_ids: Union[List[int], UnsetType] = unset,
        tiers: Union[List[AiGatewayRoutingRuleTierRequest], UnsetType] = unset,
        **kwargs,
    ):
        """
        Partial route update. Omit tiers to preserve the entire graph, including hidden selections. Saved target IDs retain omitted settings. Replacing tiers must explicitly retain or remove every hidden occurrence.

        :param description: Optional description of what the routing rule is for. Up to 500 characters.
            Omit it or send null to keep the saved description. Send an empty string to clear it.
        :type description: str, none_type, optional

        :param display_name: Optional human-readable name shown in place of the slug. Up to 100 characters on one line.
            Omit it or send null to keep the saved display name. Send an empty string to clear it.
        :type display_name: str, none_type, optional

        :param expected_updated_at: Saved route revision. A mismatched value returns 409 without changes.
        :type expected_updated_at: datetime, optional

        :param removed_target_ids: Parent-local saved occurrence IDs explicitly removed from the submitted tiers. IDs must be distinct, belong to this route, and not also be retained.
        :type removed_target_ids: [int], optional

        :param tiers:
        :type tiers: [AiGatewayRoutingRuleTierRequest], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if expected_updated_at is not unset:
            kwargs["expected_updated_at"] = expected_updated_at
        if removed_target_ids is not unset:
            kwargs["removed_target_ids"] = removed_target_ids
        if tiers is not unset:
            kwargs["tiers"] = tiers
        super().__init__(kwargs)
