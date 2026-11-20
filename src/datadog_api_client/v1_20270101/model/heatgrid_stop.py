# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.heatgrid_color import HeatgridColor


class HeatgridStop(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.heatgrid_color import HeatgridColor

        return {
            "color": (HeatgridColor,),
            "position": (float,),
        }

    attribute_map = {
        "color": "color",
        "position": "position",
    }

    def __init__(self_, color: Union[HeatgridColor, str, List[Any]], position: float, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color: Test-only generated schema for the dashboard versioning proof of concept.
        :type color: HeatgridColor

        :param position: Test-only generated schema for the dashboard versioning proof of concept.
        :type position: float
        """
        super().__init__(kwargs)

        self_.color = color
        self_.position = position
