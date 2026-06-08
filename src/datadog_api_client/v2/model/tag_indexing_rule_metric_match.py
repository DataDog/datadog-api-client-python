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


class TagIndexingRuleMetricMatch(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_queried": (bool,),
            "not_queried": (bool,),
            "not_used_in_assets": (bool,),
            "queried_window_seconds": (int,),
            "used_in_assets": (bool,),
        }

    attribute_map = {
        "is_queried": "is_queried",
        "not_queried": "not_queried",
        "not_used_in_assets": "not_used_in_assets",
        "queried_window_seconds": "queried_window_seconds",
        "used_in_assets": "used_in_assets",
    }

    def __init__(
        self_,
        is_queried: Union[bool, UnsetType] = unset,
        not_queried: Union[bool, UnsetType] = unset,
        not_used_in_assets: Union[bool, UnsetType] = unset,
        queried_window_seconds: Union[int, UnsetType] = unset,
        used_in_assets: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Criteria for matching metrics based on query state.

        :param is_queried: Match metrics that are being queried.
        :type is_queried: bool, optional

        :param not_queried: Match metrics that are not being queried.
        :type not_queried: bool, optional

        :param not_used_in_assets: Match metrics not used in any dashboards or monitors.
        :type not_used_in_assets: bool, optional

        :param queried_window_seconds: Window in seconds for evaluating query state.
        :type queried_window_seconds: int, optional

        :param used_in_assets: Match metrics used in dashboards or monitors.
        :type used_in_assets: bool, optional
        """
        if is_queried is not unset:
            kwargs["is_queried"] = is_queried
        if not_queried is not unset:
            kwargs["not_queried"] = not_queried
        if not_used_in_assets is not unset:
            kwargs["not_used_in_assets"] = not_used_in_assets
        if queried_window_seconds is not unset:
            kwargs["queried_window_seconds"] = queried_window_seconds
        if used_in_assets is not unset:
            kwargs["used_in_assets"] = used_in_assets
        super().__init__(kwargs)
