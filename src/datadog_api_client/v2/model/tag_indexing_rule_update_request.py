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
    from datadog_api_client.v2.model.tag_indexing_rule_update_data import TagIndexingRuleUpdateData


class TagIndexingRuleUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_update_data import TagIndexingRuleUpdateData

        return {
            "data": (TagIndexingRuleUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TagIndexingRuleUpdateData, **kwargs):
        """
        Request body for updating a tag indexing rule.

        :param data: Data object for updating a tag indexing rule.
        :type data: TagIndexingRuleUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
