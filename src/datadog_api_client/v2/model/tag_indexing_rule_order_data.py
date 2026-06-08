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
    from datadog_api_client.v2.model.tag_indexing_rule_order_attributes import TagIndexingRuleOrderAttributes
    from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType


class TagIndexingRuleOrderData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_order_attributes import TagIndexingRuleOrderAttributes
        from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType

        return {
            "attributes": (TagIndexingRuleOrderAttributes,),
            "type": (TagIndexingRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: TagIndexingRuleOrderAttributes, type: TagIndexingRuleType, **kwargs):
        """
        Data object for the reorder operation.

        :param attributes: Attributes for the reorder operation.
        :type attributes: TagIndexingRuleOrderAttributes

        :param type: The tag indexing rule resource type.
        :type type: TagIndexingRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
