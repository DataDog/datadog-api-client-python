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
    from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_rule import (
        ObservabilityPipelineMetricTagsProcessorRule,
    )
    from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_type import (
        ObservabilityPipelineMetricTagsProcessorType,
    )


class ObservabilityPipelineMetricTagsProcessor(ModelNormal):
    validations = {
        "rules": {
            "max_items": 100,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_rule import (
            ObservabilityPipelineMetricTagsProcessorRule,
        )
        from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_type import (
            ObservabilityPipelineMetricTagsProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "rules": ([ObservabilityPipelineMetricTagsProcessorRule],),
            "type": (ObservabilityPipelineMetricTagsProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "rules": "rules",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        rules: List[ObservabilityPipelineMetricTagsProcessorRule],
        type: ObservabilityPipelineMetricTagsProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``metric_tags`` processor filters metrics based on their tags using Datadog tag key patterns.

        **Supported pipeline types:** metrics

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which metrics this processor targets.
        :type include: str

        :param rules: A list of rules for filtering metric tags.
        :type rules: [ObservabilityPipelineMetricTagsProcessorRule]

        :param type: The processor type. The value should always be ``metric_tags``.
        :type type: ObservabilityPipelineMetricTagsProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.rules = rules
        self_.type = type
