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
    from datadog_api_client.v2.model.observability_pipeline_generated_metric import ObservabilityPipelineGeneratedMetric
    from datadog_api_client.v2.model.observability_pipeline_generate_metrics_processor_type import (
        ObservabilityPipelineGenerateMetricsProcessorType,
    )


class ObservabilityPipelineGenerateMetricsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_generated_metric import (
            ObservabilityPipelineGeneratedMetric,
        )
        from datadog_api_client.v2.model.observability_pipeline_generate_metrics_processor_type import (
            ObservabilityPipelineGenerateMetricsProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "metrics": ([ObservabilityPipelineGeneratedMetric],),
            "type": (ObservabilityPipelineGenerateMetricsProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "metrics": "metrics",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        type: ObservabilityPipelineGenerateMetricsProcessorType,
        display_name: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        metrics: Union[List[ObservabilityPipelineGeneratedMetric], UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``generate_datadog_metrics`` processor creates custom metrics from logs and sends them to Datadog.
        Metrics can be counters, gauges, or distributions and optionally grouped by log fields.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str, optional

        :param metrics: Configuration for generating individual metrics.
        :type metrics: [ObservabilityPipelineGeneratedMetric], optional

        :param type: The processor type. Always ``generate_datadog_metrics``.
        :type type: ObservabilityPipelineGenerateMetricsProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if include is not unset:
            kwargs["include"] = include
        if metrics is not unset:
            kwargs["metrics"] = metrics
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.type = type
