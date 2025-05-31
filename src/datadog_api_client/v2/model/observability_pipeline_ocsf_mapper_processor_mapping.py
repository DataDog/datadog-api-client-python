# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_mapping_mapping import (
        ObservabilityPipelineOcsfMapperProcessorMappingMapping,
    )


class ObservabilityPipelineOcsfMapperProcessorMapping(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor_mapping_mapping import (
            ObservabilityPipelineOcsfMapperProcessorMappingMapping,
        )

        return {
            "include": (str,),
            "mapping": (ObservabilityPipelineOcsfMapperProcessorMappingMapping,),
        }

    attribute_map = {
        "include": "include",
        "mapping": "mapping",
    }

    def __init__(
        self_, include: str, mapping: Union[ObservabilityPipelineOcsfMapperProcessorMappingMapping, str], **kwargs
    ):
        """
        Defines how specific events are transformed to OCSF using a mapping configuration.

        :param include: A Datadog search query used to select the logs that this mapping should apply to.
        :type include: str

        :param mapping: Defines a single mapping rule for transforming logs into the OCSF schema.
        :type mapping: ObservabilityPipelineOcsfMapperProcessorMappingMapping
        """
        super().__init__(kwargs)

        self_.include = include
        self_.mapping = mapping
