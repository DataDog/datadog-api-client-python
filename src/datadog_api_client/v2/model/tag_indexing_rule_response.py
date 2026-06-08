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
    from datadog_api_client.v2.model.tag_indexing_rule_data import TagIndexingRuleData


class TagIndexingRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_data import TagIndexingRuleData

        return {
            "data": (TagIndexingRuleData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[TagIndexingRuleData, UnsetType] = unset, **kwargs):
        """
        Response containing a single tag indexing rule.

        :param data: A tag indexing rule resource object.
        :type data: TagIndexingRuleData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
