# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class MetricDistinctVolumeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "distinct_volume": (int, none_type),
        }

    attribute_map = {
        "distinct_volume": "distinct_volume",
    }

    def __init__(self_, distinct_volume: Union[int, none_type, UnsetType] = unset, **kwargs):
        """
        Object containing the definition of a metric's distinct volume.

        :param distinct_volume: Distinct volume for the given metric. This value is ``null`` for standard metrics in organizations on
            Metric Name Pricing.
        :type distinct_volume: int, none_type, optional
        """
        if distinct_volume is not unset:
            kwargs["distinct_volume"] = distinct_volume
        super().__init__(kwargs)
