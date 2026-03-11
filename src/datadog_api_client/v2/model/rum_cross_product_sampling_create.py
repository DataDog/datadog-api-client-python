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


class RumCrossProductSamplingCreate(ModelNormal):
    validations = {
        "trace_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "trace_enabled": (bool,),
            "trace_sample_rate": (float,),
        }

    attribute_map = {
        "trace_enabled": "trace_enabled",
        "trace_sample_rate": "trace_sample_rate",
    }

    def __init__(self_, trace_sample_rate: float, trace_enabled: Union[bool, UnsetType] = unset, **kwargs):
        """
        Configuration for cross-product sampling when creating a retention filter.

        :param trace_enabled: Indicates whether trace cross-product sampling is enabled.
        :type trace_enabled: bool, optional

        :param trace_sample_rate: The percentage (0-100) of retained sessions with ingested traces whose traces are indexed.
        :type trace_sample_rate: float
        """
        if trace_enabled is not unset:
            kwargs["trace_enabled"] = trace_enabled
        super().__init__(kwargs)

        self_.trace_sample_rate = trace_sample_rate
