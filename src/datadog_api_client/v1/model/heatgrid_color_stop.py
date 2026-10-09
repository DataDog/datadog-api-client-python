# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.heatgrid_color import HeatgridColor


class HeatgridColorStop(ModelNormal):
    validations = {
        "position": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_color import HeatgridColor

        return {
            "color": (HeatgridColor,),
            "position": (int,),
        }

    attribute_map = {
        "color": "color",
        "position": "position",
    }

    def __init__(self_, color: Union[HeatgridColor, str, List[str]], position: int, **kwargs):
        """
        A position and color in a continuous gradient.

        :param color: A color string, or two color strings for the light and dark themes, in that order.
        :type color: HeatgridColor

        :param position: Position in the gradient, from 0 to 100.
        :type position: int
        """
        super().__init__(kwargs)

        self_.color = color
        self_.position = position
