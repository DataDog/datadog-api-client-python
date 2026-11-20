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
    from datadog_api_client.v1_20270101.model.comparator import Comparator


class ThresholdFormattingRule(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.comparator import Comparator

        return {
            "comparator": (Comparator,),
            "custom_bg_color": (str,),
            "custom_fg_color": (str,),
            "hide_value": (bool,),
            "highlight_row": (bool,),
            "image_url": (str,),
            "metric": (str,),
            "palette": (str,),
            "value": (float,),
        }

    attribute_map = {
        "comparator": "comparator",
        "custom_bg_color": "custom_bg_color",
        "custom_fg_color": "custom_fg_color",
        "hide_value": "hide_value",
        "highlight_row": "highlight_row",
        "image_url": "image_url",
        "metric": "metric",
        "palette": "palette",
        "value": "value",
    }

    def __init__(
        self_,
        comparator: Comparator,
        palette: str,
        value: float,
        custom_bg_color: Union[str, UnsetType] = unset,
        custom_fg_color: Union[str, UnsetType] = unset,
        hide_value: Union[bool, UnsetType] = unset,
        highlight_row: Union[bool, UnsetType] = unset,
        image_url: Union[str, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param comparator: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparator: Comparator

        :param custom_bg_color: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_bg_color: str, optional

        :param custom_fg_color: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_fg_color: str, optional

        :param hide_value: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_value: bool, optional

        :param highlight_row: Test-only generated schema for the dashboard versioning proof of concept.
        :type highlight_row: bool, optional

        :param image_url: Test-only generated schema for the dashboard versioning proof of concept.
        :type image_url: str, optional

        :param metric: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric: str, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: float
        """
        if custom_bg_color is not unset:
            kwargs["custom_bg_color"] = custom_bg_color
        if custom_fg_color is not unset:
            kwargs["custom_fg_color"] = custom_fg_color
        if hide_value is not unset:
            kwargs["hide_value"] = hide_value
        if highlight_row is not unset:
            kwargs["highlight_row"] = highlight_row
        if image_url is not unset:
            kwargs["image_url"] = image_url
        if metric is not unset:
            kwargs["metric"] = metric
        super().__init__(kwargs)

        self_.comparator = comparator
        self_.palette = palette
        self_.value = value
