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
    from datadog_api_client.v2.model.rule_attributes import RuleAttributes
    from datadog_api_client.v2.model.relationship_to_rule import RelationshipToRule
    from datadog_api_client.v2.model.rule_type import RuleType


class CreateRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_attributes import RuleAttributes
        from datadog_api_client.v2.model.relationship_to_rule import RelationshipToRule
        from datadog_api_client.v2.model.rule_type import RuleType

        return {
            "attributes": (RuleAttributes,),
            "id": (str,),
            "relationships": (RelationshipToRule,),
            "type": (RuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[RelationshipToRule, UnsetType] = unset,
        type: Union[RuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Create rule response data.

        :param attributes: Details of a rule.
        :type attributes: RuleAttributes, optional

        :param id: The unique ID for a scorecard rule.
        :type id: str, optional

        :param relationships: Scorecard create rule response relationship.
        :type relationships: RelationshipToRule, optional

        :param type: The JSON:API type for scorecard rules.
        :type type: RuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
