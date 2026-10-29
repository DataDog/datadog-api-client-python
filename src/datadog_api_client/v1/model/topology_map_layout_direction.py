# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TopologyMapLayoutDirection(ModelSimple):
    """
    Direction of ranks. For example, `top-to-bottom` places first-rank nodes at the top and last-rank nodes at the bottom.

    :param value: Must be one of ["top-to-bottom", "bottom-to-top", "left-to-right", "right-to-left"].
    :type value: str
    """

    allowed_values = {
        "top-to-bottom",
        "bottom-to-top",
        "left-to-right",
        "right-to-left",
    }
    TOP_TO_BOTTOM: ClassVar["TopologyMapLayoutDirection"]
    BOTTOM_TO_TOP: ClassVar["TopologyMapLayoutDirection"]
    LEFT_TO_RIGHT: ClassVar["TopologyMapLayoutDirection"]
    RIGHT_TO_LEFT: ClassVar["TopologyMapLayoutDirection"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TopologyMapLayoutDirection.TOP_TO_BOTTOM = TopologyMapLayoutDirection("top-to-bottom")
TopologyMapLayoutDirection.BOTTOM_TO_TOP = TopologyMapLayoutDirection("bottom-to-top")
TopologyMapLayoutDirection.LEFT_TO_RIGHT = TopologyMapLayoutDirection("left-to-right")
TopologyMapLayoutDirection.RIGHT_TO_LEFT = TopologyMapLayoutDirection("right-to-left")
