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
    from datadog_api_client.v2.model.pipeline_config_destination import PipelineConfigDestination
    from datadog_api_client.v2.model.pipeline_config_processor import PipelineConfigProcessor
    from datadog_api_client.v2.model.pipeline_config_source import PipelineConfigSource
    from datadog_api_client.v2.model.pipeline_datadog_logs_destination import PipelineDatadogLogsDestination
    from datadog_api_client.v2.model.pipeline_filter_processor import PipelineFilterProcessor
    from datadog_api_client.v2.model.parse_json_processor import ParseJSONProcessor
    from datadog_api_client.v2.model.pipeline_quota_processor import PipelineQuotaProcessor
    from datadog_api_client.v2.model.pipeline_add_fields_processor import PipelineAddFieldsProcessor
    from datadog_api_client.v2.model.pipeline_remove_fields_processor import PipelineRemoveFieldsProcessor
    from datadog_api_client.v2.model.pipeline_rename_fields_processor import PipelineRenameFieldsProcessor
    from datadog_api_client.v2.model.pipeline_kafka_source import PipelineKafkaSource
    from datadog_api_client.v2.model.pipeline_datadog_agent_source import PipelineDatadogAgentSource


class PipelineConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pipeline_config_destination import PipelineConfigDestination
        from datadog_api_client.v2.model.pipeline_config_processor import PipelineConfigProcessor
        from datadog_api_client.v2.model.pipeline_config_source import PipelineConfigSource

        return {
            "destinations": ([PipelineConfigDestination],),
            "processors": ([PipelineConfigProcessor],),
            "sources": ([PipelineConfigSource],),
        }

    attribute_map = {
        "destinations": "destinations",
        "processors": "processors",
        "sources": "sources",
    }

    def __init__(
        self_,
        destinations: List[Union[PipelineConfigDestination, PipelineDatadogLogsDestination]],
        processors: List[
            Union[
                PipelineConfigProcessor,
                PipelineFilterProcessor,
                ParseJSONProcessor,
                PipelineQuotaProcessor,
                PipelineAddFieldsProcessor,
                PipelineRemoveFieldsProcessor,
                PipelineRenameFieldsProcessor,
            ]
        ],
        sources: List[Union[PipelineConfigSource, PipelineKafkaSource, PipelineDatadogAgentSource]],
        **kwargs,
    ):
        """
        Specifies the pipeline's configuration, including its sources, processors, and destinations.

        :param destinations: A list of destination components where processed logs are sent.
        :type destinations: [PipelineConfigDestination]

        :param processors: A list of processors that transform or enrich log data.
        :type processors: [PipelineConfigProcessor]

        :param sources: A list of configured data sources for the pipeline.
        :type sources: [PipelineConfigSource]
        """
        super().__init__(kwargs)

        self_.destinations = destinations
        self_.processors = processors
        self_.sources = sources
