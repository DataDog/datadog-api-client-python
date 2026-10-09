# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.heatgrid_color import HeatgridColor


class HeatgridColorBin(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_color import HeatgridColor

        return {
            "color": (HeatgridColor,),
            "lower_bound": (float,),
        }

    attribute_map = {
        "color": "color",
        "lower_bound": "lower_bound",
    }

    def __init__(
        self_, color: Union[HeatgridColor, str, List[str]], lower_bound: Union[float, UnsetType] = unset, **kwargs
    ):
        """
        A color and optional lower threshold for a discrete bin.

        :param color: A color string, or two color strings for the light and dark themes, in that order.
        :type color: HeatgridColor

        :param lower_bound: Inclusive lower bound. Omit for the first bin.
        :type lower_bound: float, optional
        """
        if lower_bound is not unset:
            kwargs["lower_bound"] = lower_bound
        super().__init__(kwargs)

        self_.color = color
