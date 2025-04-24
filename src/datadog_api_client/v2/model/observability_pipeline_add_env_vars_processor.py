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
    from datadog_api_client.v2.model.observability_pipeline_add_env_vars_processor_type import (
        ObservabilityPipelineAddEnvVarsProcessorType,
    )
    from datadog_api_client.v2.model.observability_pipeline_add_env_vars_processor_variable import (
        ObservabilityPipelineAddEnvVarsProcessorVariable,
    )


class ObservabilityPipelineAddEnvVarsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_add_env_vars_processor_type import (
            ObservabilityPipelineAddEnvVarsProcessorType,
        )
        from datadog_api_client.v2.model.observability_pipeline_add_env_vars_processor_variable import (
            ObservabilityPipelineAddEnvVarsProcessorVariable,
        )

        return {
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineAddEnvVarsProcessorType,),
            "variables": ([ObservabilityPipelineAddEnvVarsProcessorVariable],),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
        "variables": "variables",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        type: ObservabilityPipelineAddEnvVarsProcessorType,
        variables: List[ObservabilityPipelineAddEnvVarsProcessorVariable],
        **kwargs,
    ):
        """
        The ``add_env_vars`` processor adds environment variable values to log events.

        :param id: The unique identifier for this component. Used to reference this processor in the pipeline.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the input for this processor.
        :type inputs: [str]

        :param type: The processor type. The value should always be ``add_env_vars``.
        :type type: ObservabilityPipelineAddEnvVarsProcessorType

        :param variables: A list of environment variable mappings to apply to log fields.
        :type variables: [ObservabilityPipelineAddEnvVarsProcessorVariable]
        """
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.type = type
        self_.variables = variables
