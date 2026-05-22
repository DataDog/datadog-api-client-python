# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_action import (
        ObservabilityPipelineTagCardinalityLimitProcessorAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_per_metric_mode import (
        ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_per_tag_limit import (
        ObservabilityPipelineTagCardinalityLimitProcessorPerTagLimit,
    )


class ObservabilityPipelineTagCardinalityLimitProcessorPerMetricLimit(ModelNormal):
    validations = {
        "per_tag_limits": {
            "max_items": 50,
        },
        "value_limit": {
            "inclusive_maximum": 1000000,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_action import (
            ObservabilityPipelineTagCardinalityLimitProcessorAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_per_metric_mode import (
            ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_per_tag_limit import (
            ObservabilityPipelineTagCardinalityLimitProcessorPerTagLimit,
        )

        return {
            "limit_exceeded_action": (ObservabilityPipelineTagCardinalityLimitProcessorAction,),
            "metric_name": (str,),
            "mode": (ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode,),
            "per_tag_limits": ([ObservabilityPipelineTagCardinalityLimitProcessorPerTagLimit],),
            "value_limit": (int,),
        }

    attribute_map = {
        "limit_exceeded_action": "limit_exceeded_action",
        "metric_name": "metric_name",
        "mode": "mode",
        "per_tag_limits": "per_tag_limits",
        "value_limit": "value_limit",
    }

    def __init__(
        self_,
        metric_name: str,
        mode: ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode,
        limit_exceeded_action: Union[ObservabilityPipelineTagCardinalityLimitProcessorAction, UnsetType] = unset,
        per_tag_limits: Union[List[ObservabilityPipelineTagCardinalityLimitProcessorPerTagLimit], UnsetType] = unset,
        value_limit: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A cardinality override applied to a specific metric.

        :param limit_exceeded_action: The action to take when the cardinality limit is exceeded.
        :type limit_exceeded_action: ObservabilityPipelineTagCardinalityLimitProcessorAction, optional

        :param metric_name: The name of the metric this override applies to.
        :type metric_name: str

        :param mode: How the per-metric override is applied. ``tracked`` enforces a custom limit; ``excluded`` skips the metric entirely.
        :type mode: ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode

        :param per_tag_limits: A list of per-tag cardinality overrides that apply within this metric. Must be omitted when ``mode`` is ``excluded``.
        :type per_tag_limits: [ObservabilityPipelineTagCardinalityLimitProcessorPerTagLimit], optional

        :param value_limit: The maximum number of distinct tag value combinations allowed for this metric. Required when ``mode`` is ``tracked``. Must be omitted when ``mode`` is ``excluded``.
        :type value_limit: int, optional
        """
        if limit_exceeded_action is not unset:
            kwargs["limit_exceeded_action"] = limit_exceeded_action
        if per_tag_limits is not unset:
            kwargs["per_tag_limits"] = per_tag_limits
        if value_limit is not unset:
            kwargs["value_limit"] = value_limit
        super().__init__(kwargs)

        self_.metric_name = metric_name
        self_.mode = mode
