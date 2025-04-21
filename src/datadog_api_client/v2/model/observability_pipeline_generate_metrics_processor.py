# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
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
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "metrics": ([ObservabilityPipelineGeneratedMetric],),
            "type": (ObservabilityPipelineGenerateMetricsProcessorType,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "metrics": "metrics",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        metrics: List[ObservabilityPipelineGeneratedMetric],
        type: ObservabilityPipelineGenerateMetricsProcessorType,
        **kwargs,
    ):
        """
        The ``generate_datadog_metrics`` processor creates custom metrics from logs and sends them to Datadog.
        Metrics can be counters, gauges, or distributions and optionally grouped by log fields.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this processor.
        :type inputs: [str]

        :param metrics: Configuration for generating individual metrics.
        :type metrics: [ObservabilityPipelineGeneratedMetric]

        :param type: The processor type. Always ``generate_datadog_metrics``.
        :type type: ObservabilityPipelineGenerateMetricsProcessorType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.metrics = metrics
        self_.type = type
