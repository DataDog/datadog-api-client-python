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
    from datadog_api_client.v2.model.tag_indexing_rule_update_attributes import TagIndexingRuleUpdateAttributes
    from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType


class TagIndexingRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_update_attributes import TagIndexingRuleUpdateAttributes
        from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType

        return {
            "attributes": (TagIndexingRuleUpdateAttributes,),
            "type": (TagIndexingRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: TagIndexingRuleType,
        attributes: Union[TagIndexingRuleUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a tag indexing rule.

        :param attributes: Attributes for updating a tag indexing rule. All fields are optional; omitted fields are unchanged.
        :type attributes: TagIndexingRuleUpdateAttributes, optional

        :param type: The tag indexing rule resource type.
        :type type: TagIndexingRuleType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
