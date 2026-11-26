# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScatterPlotDimension(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["color", "x", "y", "radius"].
    :type value: str
    """

    allowed_values = {
        "color",
        "x",
        "y",
        "radius",
    }
    COLOR: ClassVar["ScatterPlotDimension"]
    X: ClassVar["ScatterPlotDimension"]
    Y: ClassVar["ScatterPlotDimension"]
    RADIUS: ClassVar["ScatterPlotDimension"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScatterPlotDimension.COLOR = ScatterPlotDimension("color")
ScatterPlotDimension.X = ScatterPlotDimension("x")
ScatterPlotDimension.Y = ScatterPlotDimension("y")
ScatterPlotDimension.RADIUS = ScatterPlotDimension("radius")
