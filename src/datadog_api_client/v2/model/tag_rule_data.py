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
    from datadog_api_client.v2.model.tag_rule_attributes import TagRuleAttributes
    from datadog_api_client.v2.model.tag_rule_relationships import TagRuleRelationships
    from datadog_api_client.v2.model.tag_rule_resource_type import TagRuleResourceType


class TagRuleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_rule_attributes import TagRuleAttributes
        from datadog_api_client.v2.model.tag_rule_relationships import TagRuleRelationships
        from datadog_api_client.v2.model.tag_rule_resource_type import TagRuleResourceType

        return {
            "attributes": (TagRuleAttributes,),
            "id": (str,),
            "relationships": (TagRuleRelationships,),
            "type": (TagRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TagRuleAttributes,
        id: str,
        type: TagRuleResourceType,
        relationships: Union[TagRuleRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A tag rule resource.

        :param attributes: The attributes of a tag rule resource.
        :type attributes: TagRuleAttributes

        :param id: The unique identifier of the tag rule.
        :type id: str

        :param relationships: Related resources for a tag rule. Only present when the corresponding ``include`` query parameter is supplied.
        :type relationships: TagRuleRelationships, optional

        :param type: JSON:API resource type for a tag rule.
        :type type: TagRuleResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
