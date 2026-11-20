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
    from datadog_api_client.v1_20270101.model.distribution_scale_type import DistributionScaleType


class DistributionXAxis(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.axis_bound import AxisBound
        from datadog_api_client.v1_20270101.model.distribution_scale_type import DistributionScaleType

        return {
            "include_zero": (bool,),
            "max": (AxisBound,),
            "min": (AxisBound,),
            "num_buckets": (float,),
            "scale": (DistributionScaleType,),
        }

    attribute_map = {
        "include_zero": "include_zero",
        "max": "max",
        "min": "min",
        "num_buckets": "num_buckets",
        "scale": "scale",
    }

    def __init__(
        self_,
        include_zero: Union[bool, UnsetType] = unset,
        max: Union[AxisBound, str, float, UnsetType] = unset,
        min: Union[AxisBound, str, float, UnsetType] = unset,
        num_buckets: Union[float, UnsetType] = unset,
        scale: Union[DistributionScaleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param include_zero: Test-only generated schema for the dashboard versioning proof of concept.
        :type include_zero: bool, optional

        :param max: Test-only generated schema for the dashboard versioning proof of concept.
        :type max: AxisBound, optional

        :param min: Test-only generated schema for the dashboard versioning proof of concept.
        :type min: AxisBound, optional

        :param num_buckets: Test-only generated schema for the dashboard versioning proof of concept.
        :type num_buckets: float, optional

        :param scale: Test-only generated schema for the dashboard versioning proof of concept.
        :type scale: DistributionScaleType, optional
        """
        if include_zero is not unset:
            kwargs["include_zero"] = include_zero
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        if num_buckets is not unset:
            kwargs["num_buckets"] = num_buckets
        if scale is not unset:
            kwargs["scale"] = scale
        super().__init__(kwargs)
