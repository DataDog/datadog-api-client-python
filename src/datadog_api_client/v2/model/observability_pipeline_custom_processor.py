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
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "remaps": ([ObservabilityPipelineCustomProcessorRemap],),
            "type": (ObservabilityPipelineCustomProcessorType,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "remaps": "remaps",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        remaps: List[ObservabilityPipelineCustomProcessorRemap],
        type: ObservabilityPipelineCustomProcessorType,
        **kwargs,
    ):
        """
        The ``custom_processor`` processor transforms events using `Vector Remap Language (VRL) <https://vector.dev/docs/reference/vrl/>`_ scripts with advanced filtering capabilities.

        :param id: The unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets. This field should always be set to ``*`` for the custom_processor processor.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the input for this processor.
        :type inputs: [str]

        :param remaps: Array of VRL remap rules.
        :type remaps: [ObservabilityPipelineCustomProcessorRemap]

        :param type: The processor type. The value should always be ``custom_processor``.
        :type type: ObservabilityPipelineCustomProcessorType
        """
        super().__init__(kwargs)
        include = kwargs.get("include", "*")

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.remaps = remaps
        self_.type = type
