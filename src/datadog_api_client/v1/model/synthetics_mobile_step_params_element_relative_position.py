# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsMobileStepParamsElementRelativePosition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "x": (int,),
            "y": (int,),
        }

    attribute_map = {
        "x": "x",
        "y": "y",
    }

    def __init__(self_, x: Union[int, UnsetType] = unset, y: Union[int, UnsetType] = unset, **kwargs):
        """
        Position of the action relative to the element.

        :param x: The ``relativePosition`` on the ``x`` axis for the element.
        :type x: int, optional

        :param y: The ``relativePosition`` on the ``y`` axis for the element.
        :type y: int, optional
        """
        if x is not unset:
            kwargs["x"] = x
        if y is not unset:
            kwargs["y"] = y
        super().__init__(kwargs)
