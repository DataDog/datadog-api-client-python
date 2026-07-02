# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateSnapshotTimeseriesLegendType(ModelSimple):
    """
    The legend display type for timeseries widgets. A value of `none` hides the legend entirely; omitting the field lets the frontend choose automatically.

    :param value: Must be one of ["compact", "expanded", "none"].
    :type value: str
    """

    allowed_values = {
        "compact",
        "expanded",
        "none",
    }
    COMPACT: ClassVar["CreateSnapshotTimeseriesLegendType"]
    EXPANDED: ClassVar["CreateSnapshotTimeseriesLegendType"]
    NONE: ClassVar["CreateSnapshotTimeseriesLegendType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateSnapshotTimeseriesLegendType.COMPACT = CreateSnapshotTimeseriesLegendType("compact")
CreateSnapshotTimeseriesLegendType.EXPANDED = CreateSnapshotTimeseriesLegendType("expanded")
CreateSnapshotTimeseriesLegendType.NONE = CreateSnapshotTimeseriesLegendType("none")
