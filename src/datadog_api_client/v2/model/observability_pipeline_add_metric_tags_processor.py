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
    from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
    from datadog_api_client.v2.model.observability_pipeline_add_metric_tags_processor_type import (
        ObservabilityPipelineAddMetricTagsProcessorType,
    )


class ObservabilityPipelineAddMetricTagsProcessor(ModelNormal):
    validations = {
        "tags": {
            "max_items": 15,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
        from datadog_api_client.v2.model.observability_pipeline_add_metric_tags_processor_type import (
            ObservabilityPipelineAddMetricTagsProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "tags": ([ObservabilityPipelineFieldValue],),
            "type": (ObservabilityPipelineAddMetricTagsProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "tags": "tags",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        tags: List[ObservabilityPipelineFieldValue],
        type: ObservabilityPipelineAddMetricTagsProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``add_metric_tags`` processor adds static tags to metrics.

        **Supported pipeline types:** metrics

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Indicates whether the processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which metrics this processor targets.
        :type include: str

        :param tags: A list of static tags (key-value pairs) added to each metric processed by this component.
        :type tags: [ObservabilityPipelineFieldValue]

        :param type: The processor type. The value must be ``add_metric_tags``.
        :type type: ObservabilityPipelineAddMetricTagsProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.tags = tags
        self_.type = type
