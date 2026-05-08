# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PointPlotDimension(ModelSimple):
    """
    Dimension of the point plot.

    :param value: Must be one of ["group", "time", "y", "radius"].
    :type value: str
    """

    allowed_values = {
        "group",
        "time",
        "y",
        "radius",
    }
    GROUP: ClassVar["PointPlotDimension"]
    TIME: ClassVar["PointPlotDimension"]
    Y: ClassVar["PointPlotDimension"]
    RADIUS: ClassVar["PointPlotDimension"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PointPlotDimension.GROUP = PointPlotDimension("group")
PointPlotDimension.TIME = PointPlotDimension("time")
PointPlotDimension.Y = PointPlotDimension("y")
PointPlotDimension.RADIUS = PointPlotDimension("radius")
