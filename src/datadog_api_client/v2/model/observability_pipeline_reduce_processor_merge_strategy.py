# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_reduce_processor_merge_strategy_strategy import (
        ObservabilityPipelineReduceProcessorMergeStrategyStrategy,
    )


class ObservabilityPipelineReduceProcessorMergeStrategy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_reduce_processor_merge_strategy_strategy import (
            ObservabilityPipelineReduceProcessorMergeStrategyStrategy,
        )

        return {
            "path": (str,),
            "strategy": (ObservabilityPipelineReduceProcessorMergeStrategyStrategy,),
        }

    attribute_map = {
        "path": "path",
        "strategy": "strategy",
    }

    def __init__(self_, path: str, strategy: ObservabilityPipelineReduceProcessorMergeStrategyStrategy, **kwargs):
        """
        Defines how a specific field should be merged across grouped events.

        :param path: The field path in the log event.
        :type path: str

        :param strategy: The merge strategy to apply.
        :type strategy: ObservabilityPipelineReduceProcessorMergeStrategyStrategy
        """
        super().__init__(kwargs)

        self_.path = path
        self_.strategy = strategy
