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
    from datadog_api_client.v2.model.tag_rule_update_attributes import TagRuleUpdateAttributes
    from datadog_api_client.v2.model.tag_rule_resource_type import TagRuleResourceType


class TagRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_rule_update_attributes import TagRuleUpdateAttributes
        from datadog_api_client.v2.model.tag_rule_resource_type import TagRuleResourceType

        return {
            "attributes": (TagRuleUpdateAttributes,),
            "id": (str,),
            "type": (TagRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: TagRuleResourceType,
        attributes: Union[TagRuleUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a tag rule.

        :param attributes: Mutable attributes of a tag rule. Each field is optional; omitting a field leaves its
            current value unchanged. The ``source`` of a rule cannot be changed.
        :type attributes: TagRuleUpdateAttributes, optional

        :param id: The unique identifier of the tag rule being updated.
        :type id: str

        :param type: JSON:API resource type for a tag rule.
        :type type: TagRuleResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
