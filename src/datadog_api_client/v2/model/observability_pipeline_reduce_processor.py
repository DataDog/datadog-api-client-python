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
    from datadog_api_client.v2.model.observability_pipeline_reduce_processor_merge_strategy import (
        ObservabilityPipelineReduceProcessorMergeStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_reduce_processor_type import (
        ObservabilityPipelineReduceProcessorType,
    )


class ObservabilityPipelineReduceProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_reduce_processor_merge_strategy import (
            ObservabilityPipelineReduceProcessorMergeStrategy,
        )
        from datadog_api_client.v2.model.observability_pipeline_reduce_processor_type import (
            ObservabilityPipelineReduceProcessorType,
        )

        return {
            "group_by": ([str],),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "merge_strategies": ([ObservabilityPipelineReduceProcessorMergeStrategy],),
            "type": (ObservabilityPipelineReduceProcessorType,),
        }

    attribute_map = {
        "group_by": "group_by",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "merge_strategies": "merge_strategies",
        "type": "type",
    }

    def __init__(
        self_,
        group_by: List[str],
        id: str,
        include: str,
        inputs: List[str],
        merge_strategies: List[ObservabilityPipelineReduceProcessorMergeStrategy],
        type: ObservabilityPipelineReduceProcessorType,
        **kwargs,
    ):
        """
        The ``reduce`` processor aggregates and merges logs based on matching keys and merge strategies.

        :param group_by: A list of fields used to group log events for merging.
        :type group_by: [str]

        :param id: The unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the input for this processor.
        :type inputs: [str]

        :param merge_strategies: List of merge strategies defining how values from grouped events should be combined.
        :type merge_strategies: [ObservabilityPipelineReduceProcessorMergeStrategy]

        :param type: The processor type. The value should always be ``reduce``.
        :type type: ObservabilityPipelineReduceProcessorType
        """
        super().__init__(kwargs)

        self_.group_by = group_by
        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.merge_strategies = merge_strategies
        self_.type = type
