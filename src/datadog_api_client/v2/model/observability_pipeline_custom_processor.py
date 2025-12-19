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
    from datadog_api_client.v2.model.observability_pipeline_custom_processor_remap import (
        ObservabilityPipelineCustomProcessorRemap,
    )
    from datadog_api_client.v2.model.observability_pipeline_custom_processor_type import (
        ObservabilityPipelineCustomProcessorType,
    )


class ObservabilityPipelineCustomProcessor(ModelNormal):
    validations = {
        "remaps": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_custom_processor_remap import (
            ObservabilityPipelineCustomProcessorRemap,
        )
        from datadog_api_client.v2.model.observability_pipeline_custom_processor_type import (
            ObservabilityPipelineCustomProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "remaps": ([ObservabilityPipelineCustomProcessorRemap],),
            "type": (ObservabilityPipelineCustomProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "remaps": "remaps",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        remaps: List[ObservabilityPipelineCustomProcessorRemap],
        type: ObservabilityPipelineCustomProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``custom_processor`` processor transforms events using `Vector Remap Language (VRL) <https://vector.dev/docs/reference/vrl/>`_ scripts with advanced filtering capabilities.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets. This field should always be set to ``*`` for the custom_processor processor.
        :type include: str

        :param remaps: Array of VRL remap rules.
        :type remaps: [ObservabilityPipelineCustomProcessorRemap]

        :param type: The processor type. The value should always be ``custom_processor``.
        :type type: ObservabilityPipelineCustomProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)
        include = kwargs.get("include", "*")

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.remaps = remaps
        self_.type = type
