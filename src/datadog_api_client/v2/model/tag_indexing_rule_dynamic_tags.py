# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TagIndexingRuleDynamicTags(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "queried_tags_window_seconds": (int,),
            "related_asset_tags": (bool,),
        }

    attribute_map = {
        "queried_tags_window_seconds": "queried_tags_window_seconds",
        "related_asset_tags": "related_asset_tags",
    }

    def __init__(
        self_,
        queried_tags_window_seconds: Union[int, UnsetType] = unset,
        related_asset_tags: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for including dynamically queried tags.

        :param queried_tags_window_seconds: Window in seconds for evaluating queried tags.
        :type queried_tags_window_seconds: int, optional

        :param related_asset_tags: When true, tags from related assets are included.
        :type related_asset_tags: bool, optional
        """
        if queried_tags_window_seconds is not unset:
            kwargs["queried_tags_window_seconds"] = queried_tags_window_seconds
        if related_asset_tags is not unset:
            kwargs["related_asset_tags"] = related_asset_tags
        super().__init__(kwargs)
