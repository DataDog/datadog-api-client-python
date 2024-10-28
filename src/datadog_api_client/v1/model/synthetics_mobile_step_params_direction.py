# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMobileStepParamsDirection(ModelSimple):
    """
    The direction of the scroll for a `scrollToElement` step type.

    :param value: Must be one of ["up", "down", "left", "right"].
    :type value: str
    """

    allowed_values = {
        "up",
        "down",
        "left",
        "right",
    }
    UP: ClassVar["SyntheticsMobileStepParamsDirection"]
    DOWN: ClassVar["SyntheticsMobileStepParamsDirection"]
    LEFT: ClassVar["SyntheticsMobileStepParamsDirection"]
    RIGHT: ClassVar["SyntheticsMobileStepParamsDirection"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMobileStepParamsDirection.UP = SyntheticsMobileStepParamsDirection("up")
SyntheticsMobileStepParamsDirection.DOWN = SyntheticsMobileStepParamsDirection("down")
SyntheticsMobileStepParamsDirection.LEFT = SyntheticsMobileStepParamsDirection("left")
SyntheticsMobileStepParamsDirection.RIGHT = SyntheticsMobileStepParamsDirection("right")
