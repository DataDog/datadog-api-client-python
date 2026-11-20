# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomTopologyMapLayoutDirection(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["top-to-bottom", "bottom-to-top", "left-to-right", "right-to-left"].
    :type value: str
    """

    allowed_values = {
        "top-to-bottom",
        "bottom-to-top",
        "left-to-right",
        "right-to-left",
    }
    TOP_TO_BOTTOM: ClassVar["CustomTopologyMapLayoutDirection"]
    BOTTOM_TO_TOP: ClassVar["CustomTopologyMapLayoutDirection"]
    LEFT_TO_RIGHT: ClassVar["CustomTopologyMapLayoutDirection"]
    RIGHT_TO_LEFT: ClassVar["CustomTopologyMapLayoutDirection"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomTopologyMapLayoutDirection.TOP_TO_BOTTOM = CustomTopologyMapLayoutDirection("top-to-bottom")
CustomTopologyMapLayoutDirection.BOTTOM_TO_TOP = CustomTopologyMapLayoutDirection("bottom-to-top")
CustomTopologyMapLayoutDirection.LEFT_TO_RIGHT = CustomTopologyMapLayoutDirection("left-to-right")
CustomTopologyMapLayoutDirection.RIGHT_TO_LEFT = CustomTopologyMapLayoutDirection("right-to-left")
