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


class WidgetMarker(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "display_type": (str,),
            "label": (str,),
            "on_right_yaxis": (bool,),
            "time": (str,),
            "value": (str,),
        }

    attribute_map = {
        "display_type": "display_type",
        "label": "label",
        "on_right_yaxis": "on_right_yaxis",
        "time": "time",
        "value": "value",
    }

    def __init__(
        self_,
        value: str,
        display_type: Union[str, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        on_right_yaxis: Union[bool, UnsetType] = unset,
        time: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param display_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_type: str, optional

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str, optional

        :param on_right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type on_right_yaxis: bool, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: str, optional

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: str
        """
        if display_type is not unset:
            kwargs["display_type"] = display_type
        if label is not unset:
            kwargs["label"] = label
        if on_right_yaxis is not unset:
            kwargs["on_right_yaxis"] = on_right_yaxis
        if time is not unset:
            kwargs["time"] = time
        super().__init__(kwargs)

        self_.value = value
