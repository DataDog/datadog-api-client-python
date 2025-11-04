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


class FacetInfoResponseDataAttributesResultRange(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "max": (dict,),
            "min": (dict,),
        }

    attribute_map = {
        "max": "max",
        "min": "min",
    }

    def __init__(self_, max: Union[dict, UnsetType] = unset, min: Union[dict, UnsetType] = unset, **kwargs):
        """


        :param max:
        :type max: dict, optional

        :param min:
        :type min: dict, optional
        """
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        super().__init__(kwargs)
