# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.heatgrid_color import HeatgridColor


class HeatgridBin(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.heatgrid_color import HeatgridColor

        return {
            "color": (HeatgridColor,),
            "label": (str,),
            "lower_bound": (float,),
        }

    attribute_map = {
        "color": "color",
        "label": "label",
        "lower_bound": "lower_bound",
    }

    def __init__(
        self_,
        color: Union[HeatgridColor, str, List[Any]],
        label: Union[str, UnsetType] = unset,
        lower_bound: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color: Test-only generated schema for the dashboard versioning proof of concept.
        :type color: HeatgridColor

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str, optional

        :param lower_bound: Test-only generated schema for the dashboard versioning proof of concept.
        :type lower_bound: float, optional
        """
        if label is not unset:
            kwargs["label"] = label
        if lower_bound is not unset:
            kwargs["lower_bound"] = lower_bound
        super().__init__(kwargs)

        self_.color = color
