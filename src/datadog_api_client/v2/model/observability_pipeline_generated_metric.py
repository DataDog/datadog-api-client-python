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
    from datadog_api_client.v2.model.observability_pipeline_generated_metric_metric_type import (
        ObservabilityPipelineGeneratedMetricMetricType,
    )
    from datadog_api_client.v2.model.observability_pipeline_metric_value import ObservabilityPipelineMetricValue
    from datadog_api_client.v2.model.observability_pipeline_generated_metric_increment_by_one import (
        ObservabilityPipelineGeneratedMetricIncrementByOne,
    )
    from datadog_api_client.v2.model.observability_pipeline_generated_metric_increment_by_field import (
        ObservabilityPipelineGeneratedMetricIncrementByField,
    )


class ObservabilityPipelineGeneratedMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_generated_metric_metric_type import (
            ObservabilityPipelineGeneratedMetricMetricType,
        )
        from datadog_api_client.v2.model.observability_pipeline_metric_value import ObservabilityPipelineMetricValue

        return {
            "group_by": ([str],),
            "include": (str,),
            "metric_type": (ObservabilityPipelineGeneratedMetricMetricType,),
            "name": (str,),
            "value": (ObservabilityPipelineMetricValue,),
        }

    attribute_map = {
        "group_by": "group_by",
        "include": "include",
        "metric_type": "metric_type",
        "name": "name",
        "value": "value",
    }

    def __init__(
        self_,
        include: str,
        metric_type: ObservabilityPipelineGeneratedMetricMetricType,
        name: str,
        value: Union[
            ObservabilityPipelineMetricValue,
            ObservabilityPipelineGeneratedMetricIncrementByOne,
            ObservabilityPipelineGeneratedMetricIncrementByField,
        ],
        group_by: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a log-based custom metric, including its name, type, filter, value computation strategy,
        and optional grouping fields.

        :param group_by: Optional fields used to group the metric series.
        :type group_by: [str], optional

        :param include: Datadog filter query to match logs for metric generation.
        :type include: str

        :param metric_type: Type of metric to create.
        :type metric_type: ObservabilityPipelineGeneratedMetricMetricType

        :param name: Name of the custom metric to be created.
        :type name: str

        :param value: Specifies how the value of the generated metric is computed.
        :type value: ObservabilityPipelineMetricValue
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.include = include
        self_.metric_type = metric_type
        self_.name = name
        self_.value = value
