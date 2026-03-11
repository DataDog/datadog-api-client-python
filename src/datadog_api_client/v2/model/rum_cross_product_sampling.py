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


class RumCrossProductSampling(ModelNormal):
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

    def __init__(
        self_,
        trace_enabled: Union[bool, UnsetType] = unset,
        trace_sample_rate: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for additional APM trace data retention for sessions that match this retention filter.
        When a session matches the filter and is retained (based on ``sample_rate`` ), you can configure
        the percentage of retained sessions with ingested traces whose traces are indexed.

        :param trace_enabled: Indicates whether trace cross-product sampling is enabled. If ``false`` , no traces are indexed regardless of ``trace_sample_rate``.
        :type trace_enabled: bool, optional

        :param trace_sample_rate: The percentage (0-100) of retained sessions with ingested traces whose traces are indexed.
            For example, 25.0 means 25% of retained sessions with ingested traces have their traces indexed.
        :type trace_sample_rate: float, optional
        """
        if trace_enabled is not unset:
            kwargs["trace_enabled"] = trace_enabled
        if trace_sample_rate is not unset:
            kwargs["trace_sample_rate"] = trace_sample_rate
        super().__init__(kwargs)
