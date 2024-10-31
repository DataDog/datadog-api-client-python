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


class SyntheticsMobileStepParamsPositionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "x": (float,),
            "y": (float,),
        }

    attribute_map = {
        "x": "x",
        "y": "y",
    }

    def __init__(self_, x: Union[float, UnsetType] = unset, y: Union[float, UnsetType] = unset, **kwargs):
        """
        A description of a single position for a ``flick`` step type.

        :param x: The ``x`` position for the flick.
        :type x: float, optional

        :param y: The ``y`` position for the flick.
        :type y: float, optional
        """
        if x is not unset:
            kwargs["x"] = x
        if y is not unset:
            kwargs["y"] = y
        super().__init__(kwargs)
