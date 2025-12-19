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
    from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor_action import (
        ObservabilityPipelineDatadogTagsProcessorAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor_mode import (
        ObservabilityPipelineDatadogTagsProcessorMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor_type import (
        ObservabilityPipelineDatadogTagsProcessorType,
    )


class ObservabilityPipelineDatadogTagsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor_action import (
            ObservabilityPipelineDatadogTagsProcessorAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor_mode import (
            ObservabilityPipelineDatadogTagsProcessorMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor_type import (
            ObservabilityPipelineDatadogTagsProcessorType,
        )

        return {
            "action": (ObservabilityPipelineDatadogTagsProcessorAction,),
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "keys": ([str],),
            "mode": (ObservabilityPipelineDatadogTagsProcessorMode,),
            "type": (ObservabilityPipelineDatadogTagsProcessorType,),
        }

    attribute_map = {
        "action": "action",
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "keys": "keys",
        "mode": "mode",
        "type": "type",
    }

    def __init__(
        self_,
        action: ObservabilityPipelineDatadogTagsProcessorAction,
        enabled: bool,
        id: str,
        include: str,
        keys: List[str],
        mode: ObservabilityPipelineDatadogTagsProcessorMode,
        type: ObservabilityPipelineDatadogTagsProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``datadog_tags`` processor includes or excludes specific Datadog tags in your logs.

        :param action: The action to take on tags with matching keys.
        :type action: ObservabilityPipelineDatadogTagsProcessorAction

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param keys: A list of tag keys.
        :type keys: [str]

        :param mode: The processing mode.
        :type mode: ObservabilityPipelineDatadogTagsProcessorMode

        :param type: The processor type. The value should always be ``datadog_tags``.
        :type type: ObservabilityPipelineDatadogTagsProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.action = action
        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.keys = keys
        self_.mode = mode
        self_.type = type
