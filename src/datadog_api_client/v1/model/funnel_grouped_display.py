# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FunnelGroupedDisplay(ModelSimple):
    """
    Display mode for grouped funnel results.

    :param value: Must be one of ["stacked", "side_by_side"].
    :type value: str
    """

    allowed_values = {
        "stacked",
        "side_by_side",
    }
    STACKED: ClassVar["FunnelGroupedDisplay"]
    SIDE_BY_SIDE: ClassVar["FunnelGroupedDisplay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FunnelGroupedDisplay.STACKED = FunnelGroupedDisplay("stacked")
FunnelGroupedDisplay.SIDE_BY_SIDE = FunnelGroupedDisplay("side_by_side")
