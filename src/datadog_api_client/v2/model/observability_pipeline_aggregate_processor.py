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
    from datadog_api_client.v2.model.observability_pipeline_aggregate_processor_mode import (
        ObservabilityPipelineAggregateProcessorMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_aggregate_processor_type import (
        ObservabilityPipelineAggregateProcessorType,
    )


class ObservabilityPipelineAggregateProcessor(ModelNormal):
    validations = {
        "interval_secs": {
            "inclusive_maximum": 60,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_aggregate_processor_mode import (
            ObservabilityPipelineAggregateProcessorMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_aggregate_processor_type import (
            ObservabilityPipelineAggregateProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "interval_secs": (int,),
            "mode": (ObservabilityPipelineAggregateProcessorMode,),
            "type": (ObservabilityPipelineAggregateProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "interval_secs": "interval_secs",
        "mode": "mode",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        interval_secs: int,
        mode: ObservabilityPipelineAggregateProcessorMode,
        type: ObservabilityPipelineAggregateProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``aggregate`` processor combines metrics that share the same name and tags into a single metric over a configurable interval.

        **Supported pipeline types:** metrics

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Indicates whether the processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which metrics this processor targets.
        :type include: str

        :param interval_secs: The interval, in seconds, over which metrics are aggregated.
        :type interval_secs: int

        :param mode: The aggregation mode applied to metrics that share the same name and tags within the interval.
        :type mode: ObservabilityPipelineAggregateProcessorMode

        :param type: The processor type. The value must be ``aggregate``.
        :type type: ObservabilityPipelineAggregateProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.interval_secs = interval_secs
        self_.mode = mode
        self_.type = type
