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
    from datadog_api_client.v1_20270101.model.axis_bound import AxisBound
    from datadog_api_client.v1_20270101.model.scale_type import ScaleType


class Axis(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.axis_bound import AxisBound
        from datadog_api_client.v1_20270101.model.scale_type import ScaleType

        return {
            "include_zero": (bool,),
            "label": (str,),
            "max": (AxisBound,),
            "min": (AxisBound,),
            "scale": (ScaleType,),
            "units": (bool,),
        }

    attribute_map = {
        "include_zero": "include_zero",
        "label": "label",
        "max": "max",
        "min": "min",
        "scale": "scale",
        "units": "units",
    }

    def __init__(
        self_,
        include_zero: Union[bool, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        max: Union[AxisBound, str, float, UnsetType] = unset,
        min: Union[AxisBound, str, float, UnsetType] = unset,
        scale: Union[ScaleType, UnsetType] = unset,
        units: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param include_zero: Test-only generated schema for the dashboard versioning proof of concept.
        :type include_zero: bool, optional

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str, optional

        :param max: Test-only generated schema for the dashboard versioning proof of concept.
        :type max: AxisBound, optional

        :param min: Test-only generated schema for the dashboard versioning proof of concept.
        :type min: AxisBound, optional

        :param scale: Test-only generated schema for the dashboard versioning proof of concept.
        :type scale: ScaleType, optional

        :param units: Test-only generated schema for the dashboard versioning proof of concept.
        :type units: bool, optional
        """
        if include_zero is not unset:
            kwargs["include_zero"] = include_zero
        if label is not unset:
            kwargs["label"] = label
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        if scale is not unset:
            kwargs["scale"] = scale
        if units is not unset:
            kwargs["units"] = units
        super().__init__(kwargs)
