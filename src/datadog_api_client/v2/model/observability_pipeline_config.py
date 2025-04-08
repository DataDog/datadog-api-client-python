# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_config_destination_item import (
        ObservabilityPipelineConfigDestinationItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_config_processor_item import (
        ObservabilityPipelineConfigProcessorItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_config_source_item import (
        ObservabilityPipelineConfigSourceItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_datadog_logs_destination import (
        ObservabilityPipelineDatadogLogsDestination,
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
    from datadog_api_client.v2.model.observability_pipeline_kafka_source import ObservabilityPipelineKafkaSource
    from datadog_api_client.v2.model.observability_pipeline_datadog_agent_source import (
        ObservabilityPipelineDatadogAgentSource,
    )


class ObservabilityPipelineConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_config_destination_item import (
            ObservabilityPipelineConfigDestinationItem,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_processor_item import (
            ObservabilityPipelineConfigProcessorItem,
        )
        from datadog_api_client.v2.model.observability_pipeline_config_source_item import (
            ObservabilityPipelineConfigSourceItem,
        )

        return {
            "destinations": ([ObservabilityPipelineConfigDestinationItem],),
            "processors": ([ObservabilityPipelineConfigProcessorItem],),
            "sources": ([ObservabilityPipelineConfigSourceItem],),
        }

    attribute_map = {
        "destinations": "destinations",
        "processors": "processors",
        "sources": "sources",
    }

    def __init__(
        self_,
        destinations: List[
            Union[ObservabilityPipelineConfigDestinationItem, ObservabilityPipelineDatadogLogsDestination]
        ],
        processors: List[
            Union[
                ObservabilityPipelineConfigProcessorItem,
                ObservabilityPipelineFilterProcessor,
                ObservabilityPipelineParseJSONProcessor,
                ObservabilityPipelineQuotaProcessor,
                ObservabilityPipelineAddFieldsProcessor,
                ObservabilityPipelineRemoveFieldsProcessor,
                ObservabilityPipelineRenameFieldsProcessor,
            ]
        ],
        sources: List[
            Union[
                ObservabilityPipelineConfigSourceItem,
                ObservabilityPipelineKafkaSource,
                ObservabilityPipelineDatadogAgentSource,
            ]
        ],
        **kwargs,
    ):
        """
        Specifies the pipeline's configuration, including its sources, processors, and destinations.

        :param destinations: A list of destination components where processed logs are sent.
        :type destinations: [ObservabilityPipelineConfigDestinationItem]

        :param processors: A list of processors that transform or enrich log data.
        :type processors: [ObservabilityPipelineConfigProcessorItem]

        :param sources: A list of configured data sources for the pipeline.
        :type sources: [ObservabilityPipelineConfigSourceItem]
        """
        super().__init__(kwargs)

        self_.destinations = destinations
        self_.processors = processors
        self_.sources = sources
