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
    validations = {
        "exclude_not_queried_window_seconds": {
            "inclusive_maximum": 7776000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "exclude_not_queried_window_seconds": (int,),
            "exclude_not_used_in_assets": (bool,),
            "queried_tags_window_seconds": (int,),
            "related_asset_tags": (bool,),
        }

    attribute_map = {
        "exclude_not_queried_window_seconds": "exclude_not_queried_window_seconds",
        "exclude_not_used_in_assets": "exclude_not_used_in_assets",
        "queried_tags_window_seconds": "queried_tags_window_seconds",
        "related_asset_tags": "related_asset_tags",
    }

    def __init__(
        self_,
        exclude_not_queried_window_seconds: Union[int, UnsetType] = unset,
        exclude_not_used_in_assets: Union[bool, UnsetType] = unset,
        queried_tags_window_seconds: Union[int, UnsetType] = unset,
        related_asset_tags: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options for dynamic tag indexing applied per metric, such as tags filtered by query usage.

        Before a tag key is dropped by this rule, two grace period conditions must be met:

        #. The metric must be submitted for at least as long as the selected window.
        #. A tag key must have been submitted for at least 15 days.

        Any metric or tag key that does not meet these conditions are excluded from this
        indexing rule. The ``exclude_not_*`` fields require ``exclude_tags_mode`` to be set to ``true``.

        :param exclude_not_queried_window_seconds: Tags that have not been queried within this window are excluded from indexing. Maximum of ``7776000`` (90 days).
        :type exclude_not_queried_window_seconds: int, optional

        :param exclude_not_used_in_assets: Tags not used in any dashboards,  monitors, notebooks, or SLOs are excluded from indexing.
        :type exclude_not_used_in_assets: bool, optional

        :param queried_tags_window_seconds: Window in seconds for evaluating queried tags.
        :type queried_tags_window_seconds: int, optional

        :param related_asset_tags: When true, tags from related assets are included.
        :type related_asset_tags: bool, optional
        """
        if exclude_not_queried_window_seconds is not unset:
            kwargs["exclude_not_queried_window_seconds"] = exclude_not_queried_window_seconds
        if exclude_not_used_in_assets is not unset:
            kwargs["exclude_not_used_in_assets"] = exclude_not_used_in_assets
        if queried_tags_window_seconds is not unset:
            kwargs["queried_tags_window_seconds"] = queried_tags_window_seconds
        if related_asset_tags is not unset:
            kwargs["related_asset_tags"] = related_asset_tags
        super().__init__(kwargs)
