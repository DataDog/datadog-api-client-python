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
    from datadog_api_client.v2.model.tag_indexing_rule_attributes import TagIndexingRuleAttributes
    from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType


class TagIndexingRuleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_attributes import TagIndexingRuleAttributes
        from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType

        return {
            "attributes": (TagIndexingRuleAttributes,),
            "id": (str,),
            "type": (TagIndexingRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[TagIndexingRuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[TagIndexingRuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A tag indexing rule resource object.

        :param attributes: Attributes of a tag indexing rule.
        :type attributes: TagIndexingRuleAttributes, optional

        :param id: The unique identifier (UUID) of the tag indexing rule.
        :type id: str, optional

        :param type: The tag indexing rule resource type.
        :type type: TagIndexingRuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
