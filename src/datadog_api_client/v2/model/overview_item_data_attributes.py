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


class OverviewItemDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "value": (int,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, value: Union[int, UnsetType] = unset, **kwargs):
        """
        Attributes of a single tile in the End User Device Monitoring overview dashboard.

        :param name: Human-readable name of the overview tile.
        :type name: str, optional

        :param value: Numeric value displayed on the overview tile.
        :type value: int, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
