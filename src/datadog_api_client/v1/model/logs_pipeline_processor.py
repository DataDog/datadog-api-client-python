# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_filter import LogsFilter
    from datadog_api_client.v1.model.logs_pipeline_processor_type import LogsPipelineProcessorType
    from datadog_api_client.v1.model.logs_processor import LogsProcessor

    globals()["LogsFilter"] = LogsFilter
    globals()["LogsPipelineProcessorType"] = LogsPipelineProcessorType
    globals()["LogsProcessor"] = LogsProcessor


class LogsPipelineProcessor(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "filter": (LogsFilter,),
            "is_enabled": (bool,),
            "name": (str,),
            "processors": ([LogsProcessor],),
            "type": (LogsPipelineProcessorType,),
        }

    attribute_map = {
        "type": "type",
        "filter": "filter",
        "is_enabled": "is_enabled",
        "name": "name",
        "processors": "processors",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """LogsPipelineProcessor - a model defined in OpenAPI


        :type type: LogsPipelineProcessorType

        :type filter: LogsFilter, optional

        :param is_enabled: Whether or not the processor is enabled. If omitted the server will use the default value of False.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param processors: Ordered list of processors in this pipeline.
        :type processors: [LogsProcessor], optional
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
