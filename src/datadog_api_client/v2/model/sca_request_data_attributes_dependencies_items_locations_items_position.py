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


class ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition(ModelNormal):
    validations = {
        "col": {
            "inclusive_maximum": 2147483647,
        },
        "line": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "col": (int,),
            "line": (int,),
        }

    attribute_map = {
        "col": "col",
        "line": "line",
    }

    def __init__(self_, col: Union[int, UnsetType] = unset, line: Union[int, UnsetType] = unset, **kwargs):
        """


        :param col:
        :type col: int, optional

        :param line:
        :type line: int, optional
        """
        if col is not unset:
            kwargs["col"] = col
        if line is not unset:
            kwargs["line"] = line
        super().__init__(kwargs)
