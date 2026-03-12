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
        The configuration for cross-product retention filters.

        :param trace_enabled: Whether the cross-product retention filter for APM traces is enabled.
        :type trace_enabled: bool, optional

        :param trace_sample_rate: The sample rate for the APM cross-product retention filter, between 0 and 100.
        :type trace_sample_rate: float
        """
        if trace_enabled is not unset:
            kwargs["trace_enabled"] = trace_enabled
        super().__init__(kwargs)

        self_.trace_sample_rate = trace_sample_rate
