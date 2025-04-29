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
    from datadog_api_client.v2.model.observability_pipeline_generated_metric_increment_by_field_strategy import (
        ObservabilityPipelineGeneratedMetricIncrementByFieldStrategy,
    )


class ObservabilityPipelineGeneratedMetricIncrementByField(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_generated_metric_increment_by_field_strategy import (
            ObservabilityPipelineGeneratedMetricIncrementByFieldStrategy,
        )

        return {
            "field": (str,),
            "strategy": (ObservabilityPipelineGeneratedMetricIncrementByFieldStrategy,),
        }

    attribute_map = {
        "field": "field",
        "strategy": "strategy",
    }

    def __init__(self_, field: str, strategy: ObservabilityPipelineGeneratedMetricIncrementByFieldStrategy, **kwargs):
        """
        Strategy that increments a generated metric based on the value of a log field.

        :param field: Name of the log field containing the numeric value to increment the metric by.
        :type field: str

        :param strategy: Uses a numeric field in the log event as the metric increment.
        :type strategy: ObservabilityPipelineGeneratedMetricIncrementByFieldStrategy
        """
        super().__init__(kwargs)

        self_.field = field
        self_.strategy = strategy
