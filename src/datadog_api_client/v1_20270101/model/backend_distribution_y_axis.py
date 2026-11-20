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
    from datadog_api_client.v1.model.backend_distribution_y_axis20270101_max import BackendDistributionYAxis20270101Max
    from datadog_api_client.v1.model.backend_distribution_y_axis20270101_min import BackendDistributionYAxis20270101Min
    from datadog_api_client.v1_20270101.model.backend_distribution_y_axis_scale import BackendDistributionYAxisScale


class BackendDistributionYAxis(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.backend_distribution_y_axis20270101_max import (
            BackendDistributionYAxis20270101Max,
        )
        from datadog_api_client.v1.model.backend_distribution_y_axis20270101_min import (
            BackendDistributionYAxis20270101Min,
        )
        from datadog_api_client.v1_20270101.model.backend_distribution_y_axis_scale import BackendDistributionYAxisScale

        return {
            "include_zero": (bool,),
            "label": (str,),
            "max": (BackendDistributionYAxis20270101Max,),
            "min": (BackendDistributionYAxis20270101Min,),
            "scale": (BackendDistributionYAxisScale,),
            "show_unit": (bool,),
        }

    attribute_map = {
        "include_zero": "include_zero",
        "label": "label",
        "max": "max",
        "min": "min",
        "scale": "scale",
        "show_unit": "show_unit",
    }

    def __init__(
        self_,
        include_zero: Union[bool, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        max: Union[BackendDistributionYAxis20270101Max, str, float, UnsetType] = unset,
        min: Union[BackendDistributionYAxis20270101Min, str, float, UnsetType] = unset,
        scale: Union[BackendDistributionYAxisScale, UnsetType] = unset,
        show_unit: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param include_zero: Test-only generated schema for the dashboard versioning proof of concept.
        :type include_zero: bool, optional

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str, optional

        :param max: Test-only generated schema for the dashboard versioning proof of concept.
        :type max: BackendDistributionYAxis20270101Max, optional

        :param min: Test-only generated schema for the dashboard versioning proof of concept.
        :type min: BackendDistributionYAxis20270101Min, optional

        :param scale: Test-only generated schema for the dashboard versioning proof of concept.
        :type scale: BackendDistributionYAxisScale, optional

        :param show_unit: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_unit: bool, optional
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
        if show_unit is not unset:
            kwargs["show_unit"] = show_unit
        super().__init__(kwargs)
