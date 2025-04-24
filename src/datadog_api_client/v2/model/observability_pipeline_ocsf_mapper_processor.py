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
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_mapping import (
        ObservabilityPipelineOcsfMapperProcessorMapping,
    )
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_type import (
        ObservabilityPipelineOcsfMapperProcessorType,
    )


class ObservabilityPipelineOcsfMapperProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_mapping import (
            ObservabilityPipelineOcsfMapperProcessorMapping,
        )
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_type import (
            ObservabilityPipelineOcsfMapperProcessorType,
        )

        return {
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "mappings": ([ObservabilityPipelineOcsfMapperProcessorMapping],),
            "type": (ObservabilityPipelineOcsfMapperProcessorType,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "mappings": "mappings",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        mappings: List[ObservabilityPipelineOcsfMapperProcessorMapping],
        type: ObservabilityPipelineOcsfMapperProcessorType,
        **kwargs,
    ):
        """
        The ``ocsf_mapper`` processor transforms logs into the OCSF schema using a predefined mapping configuration.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this processor.
        :type inputs: [str]

        :param mappings: A list of mapping rules to convert events to the OCSF format.
        :type mappings: [ObservabilityPipelineOcsfMapperProcessorMapping]

        :param type: The processor type. The value should always be ``ocsf_mapper``.
        :type type: ObservabilityPipelineOcsfMapperProcessorType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.mappings = mappings
        self_.type = type
