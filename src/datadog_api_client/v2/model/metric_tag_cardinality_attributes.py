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


class MetricTagCardinalityAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cardinality_delta": (int,),
        }

    attribute_map = {
        "cardinality_delta": "cardinality_delta",
    }

    def __init__(self_, cardinality_delta: Union[int, UnsetType] = unset, **kwargs):
        """
        An object containing properties related to the tag key

        :param cardinality_delta: This describes the recent change in the tag keys cardinality
        :type cardinality_delta: int, optional
        """
        if cardinality_delta is not unset:
            kwargs["cardinality_delta"] = cardinality_delta
        super().__init__(kwargs)
