# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_aggregate_processor_aggregation_timing_type import (
        ObservabilityPipelineAggregateProcessorAggregationTimingType,
    )


class ObservabilityPipelineAggregateProcessorAggregationTiming(ModelNormal):
    validations = {
        "allowed_lateness_secs": {
            "inclusive_maximum": 3600,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_aggregate_processor_aggregation_timing_type import (
            ObservabilityPipelineAggregateProcessorAggregationTimingType,
        )

        return {
            "allowed_lateness_secs": (int,),
            "type": (ObservabilityPipelineAggregateProcessorAggregationTimingType,),
        }

    attribute_map = {
        "allowed_lateness_secs": "allowed_lateness_secs",
        "type": "type",
    }

    def __init__(
        self_,
        type: ObservabilityPipelineAggregateProcessorAggregationTimingType,
        allowed_lateness_secs: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configures how metrics are assigned to aggregation windows. When omitted, metrics are grouped using system time.

        :param allowed_lateness_secs: Grace period, in seconds, for late-arriving metrics when using event time. Defaults to 10 seconds when omitted.
        :type allowed_lateness_secs: int, optional

        :param type: Determines whether metrics are assigned to aggregation windows based on when they are processed or their timestamps.
        :type type: ObservabilityPipelineAggregateProcessorAggregationTimingType
        """
        if allowed_lateness_secs is not unset:
            kwargs["allowed_lateness_secs"] = allowed_lateness_secs
        super().__init__(kwargs)

        self_.type = type
