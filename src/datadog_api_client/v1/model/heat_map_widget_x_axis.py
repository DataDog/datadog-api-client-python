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


class HeatMapWidgetXAxis(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "num_buckets": (int,),
        }

    attribute_map = {
        "num_buckets": "num_buckets",
    }

    def __init__(self_, num_buckets: Union[int, UnsetType] = unset, **kwargs):
        """
        X Axis controls for the heat map widget.

        :param num_buckets: Number of time buckets to target, also known as the resolution of the time bins. This is only applicable for distribution of points (group distributions use the roll-up modifier).
        :type num_buckets: int, optional
        """
        if num_buckets is not unset:
            kwargs["num_buckets"] = num_buckets
        super().__init__(kwargs)
