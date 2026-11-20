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


class SunburstKnownLegend20270101OneOf4462427680(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "hide_percent": (bool,),
            "hide_value": (bool,),
            "type": (SunburstKnownLegendAnyOfAnyOfItemType4452235232,),
        }

    attribute_map = {
        "hide_percent": "hide_percent",
        "hide_value": "hide_value",
        "type": "type",
    }

    def __init__(
        self_,
        type: SunburstKnownLegendAnyOfAnyOfItemType4452235232,
        hide_percent: Union[bool, UnsetType] = unset,
        hide_value: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param hide_percent: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_percent: bool, optional

        :param hide_value: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_value: bool, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: SunburstKnownLegendAnyOfAnyOfItemType4452235232
        """
        if hide_percent is not unset:
            kwargs["hide_percent"] = hide_percent
        if hide_value is not unset:
            kwargs["hide_value"] = hide_value
        super().__init__(kwargs)

        self_.type = type
