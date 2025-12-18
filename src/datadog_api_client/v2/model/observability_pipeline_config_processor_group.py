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
    from datadog_api_client.v2.model.observability_pipeline_config_processor_item import (
        ObservabilityPipelineConfigProcessorItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_filter_processor import ObservabilityPipelineFilterProcessor
    from datadog_api_client.v2.model.observability_pipeline_parse_json_processor import (
        ObservabilityPipelineParseJSONProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_quota_processor import ObservabilityPipelineQuotaProcessor
    from datadog_api_client.v2.model.observability_pipeline_add_fields_processor import (
        ObservabilityPipelineAddFieldsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor import (
        ObservabilityPipelineRemoveFieldsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor import (
        ObservabilityPipelineRenameFieldsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_generate_metrics_processor import (
        ObservabilityPipelineGenerateMetricsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_sample_processor import ObservabilityPipelineSampleProcessor
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor import (
        ObservabilityPipelineParseGrokProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor import (
        ObservabilityPipelineSensitiveDataScannerProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_ocsf_mapper_processor import (
        ObservabilityPipelineOcsfMapperProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_add_env_vars_processor import (
        ObservabilityPipelineAddEnvVarsProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_dedupe_processor import ObservabilityPipelineDedupeProcessor
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_processor import (
        ObservabilityPipelineEnrichmentTableProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_reduce_processor import ObservabilityPipelineReduceProcessor
    from datadog_api_client.v2.model.observability_pipeline_throttle_processor import (
        ObservabilityPipelineThrottleProcessor,
    )
    from datadog_api_client.v2.model.observability_pipeline_custom_processor import ObservabilityPipelineCustomProcessor
    from datadog_api_client.v2.model.observability_pipeline_datadog_tags_processor import (
        ObservabilityPipelineDatadogTagsProcessor,
    )


class ObservabilityPipelineConfigProcessorGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_config_processor_item import (
            ObservabilityPipelineConfigProcessorItem,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "processors": ([ObservabilityPipelineConfigProcessorItem],),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "processors": "processors",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        inputs: List[str],
        processors: List[
            Union[
                ObservabilityPipelineConfigProcessorItem,
                ObservabilityPipelineFilterProcessor,
                ObservabilityPipelineParseJSONProcessor,
                ObservabilityPipelineQuotaProcessor,
                ObservabilityPipelineAddFieldsProcessor,
                ObservabilityPipelineRemoveFieldsProcessor,
                ObservabilityPipelineRenameFieldsProcessor,
                ObservabilityPipelineGenerateMetricsProcessor,
                ObservabilityPipelineSampleProcessor,
                ObservabilityPipelineParseGrokProcessor,
                ObservabilityPipelineSensitiveDataScannerProcessor,
                ObservabilityPipelineOcsfMapperProcessor,
                ObservabilityPipelineAddEnvVarsProcessor,
                ObservabilityPipelineDedupeProcessor,
                ObservabilityPipelineEnrichmentTableProcessor,
                ObservabilityPipelineReduceProcessor,
                ObservabilityPipelineThrottleProcessor,
                ObservabilityPipelineCustomProcessor,
                ObservabilityPipelineDatadogTagsProcessor,
            ]
        ],
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A group of processors.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor group is enabled.
        :type enabled: bool

        :param id: The unique identifier for the processor group.
        :type id: str

        :param include: Conditional expression for when this processor group should execute.
        :type include: str

        :param inputs: A list of IDs for components whose output is used as the input for this processor group.
        :type inputs: [str]

        :param processors: Processors applied sequentially within this group. Events flow through each processor in order.
        :type processors: [ObservabilityPipelineConfigProcessorItem]
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.processors = processors
