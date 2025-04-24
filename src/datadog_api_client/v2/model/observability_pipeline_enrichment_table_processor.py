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
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file import (
        ObservabilityPipelineEnrichmentTableFile,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_geo_ip import (
        ObservabilityPipelineEnrichmentTableGeoIp,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor_type import (
        ObservabilityPipelineEnrichmentTableProcessorType,
    )


class ObservabilityPipelineEnrichmentTableProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file import (
            ObservabilityPipelineEnrichmentTableFile,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_geo_ip import (
            ObservabilityPipelineEnrichmentTableGeoIp,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor_type import (
            ObservabilityPipelineEnrichmentTableProcessorType,
        )

        return {
            "file": (ObservabilityPipelineEnrichmentTableFile,),
            "geoip": (ObservabilityPipelineEnrichmentTableGeoIp,),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "target": (str,),
            "type": (ObservabilityPipelineEnrichmentTableProcessorType,),
        }

    attribute_map = {
        "file": "file",
        "geoip": "geoip",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        target: str,
        type: ObservabilityPipelineEnrichmentTableProcessorType,
        file: Union[ObservabilityPipelineEnrichmentTableFile, UnsetType] = unset,
        geoip: Union[ObservabilityPipelineEnrichmentTableGeoIp, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``enrichment_table`` processor enriches logs using a static CSV file or GeoIP database.

        :param file: Defines a static enrichment table loaded from a CSV file.
        :type file: ObservabilityPipelineEnrichmentTableFile, optional

        :param geoip: Uses a GeoIP database to enrich logs based on an IP field.
        :type geoip: ObservabilityPipelineEnrichmentTableGeoIp, optional

        :param id: The unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the input for this processor.
        :type inputs: [str]

        :param target: Path where enrichment results should be stored in the log.
        :type target: str

        :param type: The processor type. The value should always be ``enrichment_table``.
        :type type: ObservabilityPipelineEnrichmentTableProcessorType
        """
        if file is not unset:
            kwargs["file"] = file
        if geoip is not unset:
            kwargs["geoip"] = geoip
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.target = target
        self_.type = type
