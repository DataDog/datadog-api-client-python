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
    from datadog_api_client.v2.model.routing_rule_relationships_policy_data_type import (
        RoutingRuleRelationshipsPolicyDataType,
    )


class RoutingRuleRelationshipsPolicyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.routing_rule_relationships_policy_data_type import (
            RoutingRuleRelationshipsPolicyDataType,
        )

        return {
            "id": (str,),
            "type": (RoutingRuleRelationshipsPolicyDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: RoutingRuleRelationshipsPolicyDataType, **kwargs):
        """
        Represents the policy data reference, containing the policy's ID and resource type.

        :param id: Specifies the unique identifier of the policy.
        :type id: str

        :param type: Indicates that the resource is of type 'policies'.
        :type type: RoutingRuleRelationshipsPolicyDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
