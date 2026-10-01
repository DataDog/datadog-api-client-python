# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_file import (
        ObservabilityPipelineMetricEnrichmentTableFile,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor_type import (
        ObservabilityPipelineEnrichmentTableProcessorType,
    )


class ObservabilityPipelineMetricEnrichmentTableFileProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_file import (
            ObservabilityPipelineMetricEnrichmentTableFile,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor_type import (
            ObservabilityPipelineEnrichmentTableProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "file": (ObservabilityPipelineMetricEnrichmentTableFile,),
            "id": (str,),
            "include": (str,),
            "type": (ObservabilityPipelineEnrichmentTableProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "file": "file",
        "id": "id",
        "include": "include",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        file: ObservabilityPipelineMetricEnrichmentTableFile,
        id: str,
        include: str,
        type: ObservabilityPipelineEnrichmentTableProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An ``enrichment_table`` processor that enriches metrics using a static CSV file.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Indicates whether the processor is enabled.
        :type enabled: bool

        :param file: Defines a static enrichment table loaded from a CSV file for metric enrichment.
        :type file: ObservabilityPipelineMetricEnrichmentTableFile

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component
            (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which metrics this processor targets.
        :type include: str

        :param type: The processor type. The value should always be ``enrichment_table``.
        :type type: ObservabilityPipelineEnrichmentTableProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.file = file
        self_.id = id
        self_.include = include
        self_.type = type
