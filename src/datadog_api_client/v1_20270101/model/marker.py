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


class Marker(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "display_type": (str,),
            "from_ts": (str,),
            "is_hovered": (bool,),
            "label": (str,),
            "max": (float,),
            "min": (float,),
            "on_right_yaxis": (bool,),
            "time": (str,),
            "to_ts": (str,),
            "ts": (str,),
            "type": (str,),
            "val": (float,),
            "value": (str,),
        }

    attribute_map = {
        "display_type": "display_type",
        "from_ts": "from_ts",
        "is_hovered": "is_hovered",
        "label": "label",
        "max": "max",
        "min": "min",
        "on_right_yaxis": "on_right_yaxis",
        "time": "time",
        "to_ts": "to_ts",
        "ts": "ts",
        "type": "type",
        "val": "val",
        "value": "value",
    }

    def __init__(
        self_,
        display_type: Union[str, UnsetType] = unset,
        from_ts: Union[str, UnsetType] = unset,
        is_hovered: Union[bool, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        max: Union[float, UnsetType] = unset,
        min: Union[float, UnsetType] = unset,
        on_right_yaxis: Union[bool, UnsetType] = unset,
        time: Union[str, UnsetType] = unset,
        to_ts: Union[str, UnsetType] = unset,
        ts: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        val: Union[float, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param display_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_type: str, optional

        :param from_ts: Test-only generated schema for the dashboard versioning proof of concept.
        :type from_ts: str, optional

        :param is_hovered: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_hovered: bool, optional

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str, optional

        :param max: Test-only generated schema for the dashboard versioning proof of concept.
        :type max: float, optional

        :param min: Test-only generated schema for the dashboard versioning proof of concept.
        :type min: float, optional

        :param on_right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type on_right_yaxis: bool, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: str, optional

        :param to_ts: Test-only generated schema for the dashboard versioning proof of concept.
        :type to_ts: str, optional

        :param ts: Test-only generated schema for the dashboard versioning proof of concept.
        :type ts: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: str, optional

        :param val: Test-only generated schema for the dashboard versioning proof of concept.
        :type val: float, optional

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: str, optional
        """
        if display_type is not unset:
            kwargs["display_type"] = display_type
        if from_ts is not unset:
            kwargs["from_ts"] = from_ts
        if is_hovered is not unset:
            kwargs["is_hovered"] = is_hovered
        if label is not unset:
            kwargs["label"] = label
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        if on_right_yaxis is not unset:
            kwargs["on_right_yaxis"] = on_right_yaxis
        if time is not unset:
            kwargs["time"] = time
        if to_ts is not unset:
            kwargs["to_ts"] = to_ts
        if ts is not unset:
            kwargs["ts"] = ts
        if type is not unset:
            kwargs["type"] = type
        if val is not unset:
            kwargs["val"] = val
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
