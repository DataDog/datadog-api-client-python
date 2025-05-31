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
    from datadog_api_client.v2.model.observability_pipeline_generated_metric_increment_by_one_strategy import (
        ObservabilityPipelineGeneratedMetricIncrementByOneStrategy,
    )


class ObservabilityPipelineGeneratedMetricIncrementByOne(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_generated_metric_increment_by_one_strategy import (
            ObservabilityPipelineGeneratedMetricIncrementByOneStrategy,
        )

        return {
            "strategy": (ObservabilityPipelineGeneratedMetricIncrementByOneStrategy,),
        }

    attribute_map = {
        "strategy": "strategy",
    }

    def __init__(self_, strategy: ObservabilityPipelineGeneratedMetricIncrementByOneStrategy, **kwargs):
        """
        Strategy that increments a generated metric by one for each matching event.

        :param strategy: Increments the metric by 1 for each matching event.
        :type strategy: ObservabilityPipelineGeneratedMetricIncrementByOneStrategy
        """
        super().__init__(kwargs)

        self_.strategy = strategy
