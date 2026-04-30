# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PointPlotProjectionType(ModelSimple):
    """
    Type of the projection.

    :param value: If omitted defaults to "point_plot". Must be one of ["point_plot"].
    :type value: str
    """

    allowed_values = {
        "point_plot",
    }
    POINT_PLOT: ClassVar["PointPlotProjectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PointPlotProjectionType.POINT_PLOT = PointPlotProjectionType("point_plot")
