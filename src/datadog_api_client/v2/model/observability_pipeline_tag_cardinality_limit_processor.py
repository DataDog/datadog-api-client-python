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
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_per_metric_limit import (
        ObservabilityPipelineTagCardinalityLimitProcessorPerMetricLimit,
    )
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_tracking_mode import (
        ObservabilityPipelineTagCardinalityLimitProcessorTrackingMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_type import (
        ObservabilityPipelineTagCardinalityLimitProcessorType,
    )


class ObservabilityPipelineTagCardinalityLimitProcessor(ModelNormal):
    validations = {
        "per_metric_limits": {
            "max_items": 100,
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
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_per_metric_limit import (
            ObservabilityPipelineTagCardinalityLimitProcessorPerMetricLimit,
        )
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_tracking_mode import (
            ObservabilityPipelineTagCardinalityLimitProcessorTrackingMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_type import (
            ObservabilityPipelineTagCardinalityLimitProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "limit_exceeded_action": (ObservabilityPipelineTagCardinalityLimitProcessorAction,),
            "per_metric_limits": ([ObservabilityPipelineTagCardinalityLimitProcessorPerMetricLimit],),
            "tracking_mode": (ObservabilityPipelineTagCardinalityLimitProcessorTrackingMode,),
            "type": (ObservabilityPipelineTagCardinalityLimitProcessorType,),
            "value_limit": (int,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "limit_exceeded_action": "limit_exceeded_action",
        "per_metric_limits": "per_metric_limits",
        "tracking_mode": "tracking_mode",
        "type": "type",
        "value_limit": "value_limit",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        limit_exceeded_action: ObservabilityPipelineTagCardinalityLimitProcessorAction,
        tracking_mode: ObservabilityPipelineTagCardinalityLimitProcessorTrackingMode,
        type: ObservabilityPipelineTagCardinalityLimitProcessorType,
        value_limit: int,
        display_name: Union[str, UnsetType] = unset,
        per_metric_limits: Union[
            List[ObservabilityPipelineTagCardinalityLimitProcessorPerMetricLimit], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The ``tag_cardinality_limit`` processor caps the number of distinct tag value combinations on metrics, dropping tags or events once the limit is exceeded.

        **Supported pipeline types:** metrics

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Indicates whether the processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which metrics this processor targets.
        :type include: str

        :param limit_exceeded_action: The action to take when the cardinality limit is exceeded.
        :type limit_exceeded_action: ObservabilityPipelineTagCardinalityLimitProcessorAction

        :param per_metric_limits: A list of per-metric cardinality overrides that take precedence over the default ``value_limit``.
        :type per_metric_limits: [ObservabilityPipelineTagCardinalityLimitProcessorPerMetricLimit], optional

        :param tracking_mode: Controls whether the processor uses exact or probabilistic tag tracking.
        :type tracking_mode: ObservabilityPipelineTagCardinalityLimitProcessorTrackingMode

        :param type: The processor type. The value must be ``tag_cardinality_limit``.
        :type type: ObservabilityPipelineTagCardinalityLimitProcessorType

        :param value_limit: The default maximum number of distinct tag value combinations allowed per metric.
        :type value_limit: int
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if per_metric_limits is not unset:
            kwargs["per_metric_limits"] = per_metric_limits
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.limit_exceeded_action = limit_exceeded_action
        self_.tracking_mode = tracking_mode
        self_.type = type
        self_.value_limit = value_limit
