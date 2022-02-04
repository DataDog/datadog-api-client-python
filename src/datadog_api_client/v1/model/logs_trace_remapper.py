# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_trace_remapper_type import LogsTraceRemapperType

    globals()["LogsTraceRemapperType"] = LogsTraceRemapperType


class LogsTraceRemapper(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "is_enabled": (bool,),
            "name": (str,),
            "sources": ([str],),
            "type": (LogsTraceRemapperType,),
        }

    attribute_map = {
        "type": "type",
        "is_enabled": "is_enabled",
        "name": "name",
        "sources": "sources",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """LogsTraceRemapper - a model defined in OpenAPI


        :type type: LogsTraceRemapperType

        :param is_enabled: Whether or not the processor is enabled. If omitted the server will use the default value of False.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param sources: Array of source attributes. If omitted the server will use the default value of ["dd.trace_id"].
        :type sources: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsTraceRemapper, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
