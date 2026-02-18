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
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_field_mapping import (
        ObservabilityPipelineOcsfMappingCustomFieldMapping,
    )
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_metadata import (
        ObservabilityPipelineOcsfMappingCustomMetadata,
    )


class ObservabilityPipelineOcsfMappingCustom(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_field_mapping import (
            ObservabilityPipelineOcsfMappingCustomFieldMapping,
        )
        from datadog_api_client.v2.model.observability_pipeline_ocsf_mapping_custom_metadata import (
            ObservabilityPipelineOcsfMappingCustomMetadata,
        )

        return {
            "mapping": ([ObservabilityPipelineOcsfMappingCustomFieldMapping],),
            "metadata": (ObservabilityPipelineOcsfMappingCustomMetadata,),
            "version": (int,),
        }

    attribute_map = {
        "mapping": "mapping",
        "metadata": "metadata",
        "version": "version",
    }

    def __init__(
        self_,
        mapping: List[ObservabilityPipelineOcsfMappingCustomFieldMapping],
        metadata: ObservabilityPipelineOcsfMappingCustomMetadata,
        version: int,
        **kwargs,
    ):
        """
        Custom OCSF mapping configuration for transforming logs.

        :param mapping: A list of field mapping rules for transforming log fields to OCSF schema fields.
        :type mapping: [ObservabilityPipelineOcsfMappingCustomFieldMapping]

        :param metadata: Metadata for the custom OCSF mapping.
        :type metadata: ObservabilityPipelineOcsfMappingCustomMetadata

        :param version: The version of the custom mapping configuration.
        :type version: int
        """
        super().__init__(kwargs)

        self_.mapping = mapping
        self_.metadata = metadata
        self_.version = version
