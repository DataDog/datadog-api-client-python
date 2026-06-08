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
    from datadog_api_client.v2.model.tag_indexing_rule_options_data import TagIndexingRuleOptionsData


class TagIndexingRuleOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_options_data import TagIndexingRuleOptionsData

        return {
            "data": (TagIndexingRuleOptionsData,),
            "version": (int,),
        }

    attribute_map = {
        "data": "data",
        "version": "version",
    }

    def __init__(
        self_,
        data: Union[TagIndexingRuleOptionsData, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Versioned configuration options for a tag indexing rule.

        :param data: Data payload for tag indexing rule options.
        :type data: TagIndexingRuleOptionsData, optional

        :param version: Options schema version. Only ``1`` is supported.
        :type version: int, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
