# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsPipelineProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_filter import LogsFilter
        from datadog_api_client.v1.model.logs_processor import LogsProcessor
        from datadog_api_client.v1.model.logs_pipeline_processor_type import LogsPipelineProcessorType

        return {
            "filter": (LogsFilter,),
            "is_enabled": (bool,),
            "name": (str,),
            "processors": ([LogsProcessor],),
            "type": (LogsPipelineProcessorType,),
        }

    attribute_map = {
        "filter": "filter",
        "is_enabled": "is_enabled",
        "name": "name",
        "processors": "processors",
        "type": "type",
    }

    def __init__(self, type, *args, **kwargs):
        """
        Nested Pipelines are pipelines within a pipeline. Use Nested Pipelines to split the processing into two steps.
        For example, first use a high-level filtering such as team and then a second level of filtering based on the
        integration, service, or any other tag or attribute.

        A pipeline can contain Nested Pipelines and Processors whereas a Nested Pipeline can only contain Processors.

        :param filter: Filter for logs.
        :type filter: LogsFilter, optional

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param processors: Ordered list of processors in this pipeline.
        :type processors: [LogsProcessor], optional

        :param type: Type of logs pipeline processor.
        :type type: LogsPipelineProcessorType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsPipelineProcessor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
