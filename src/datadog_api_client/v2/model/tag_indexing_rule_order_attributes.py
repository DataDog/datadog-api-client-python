# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TagIndexingRuleOrderAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rule_ids": ([str],),
        }

    attribute_map = {
        "rule_ids": "rule_ids",
    }

    def __init__(self_, rule_ids: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Attributes for the reorder operation.

        :param rule_ids: Ordered list of tag indexing rule UUIDs. The server assigns rule_order 1, 2, … matching position in this list.
        :type rule_ids: [str], optional
        """
        if rule_ids is not unset:
            kwargs["rule_ids"] = rule_ids
        super().__init__(kwargs)
