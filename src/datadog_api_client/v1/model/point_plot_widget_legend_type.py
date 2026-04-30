# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PointPlotWidgetLegendType(ModelSimple):
    """
    Type of legend to show for the point plot widget.

    :param value: Must be one of ["automatic", "none"].
    :type value: str
    """

    allowed_values = {
        "automatic",
        "none",
    }
    AUTOMATIC: ClassVar["PointPlotWidgetLegendType"]
    NONE: ClassVar["PointPlotWidgetLegendType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PointPlotWidgetLegendType.AUTOMATIC = PointPlotWidgetLegendType("automatic")
PointPlotWidgetLegendType.NONE = PointPlotWidgetLegendType("none")
