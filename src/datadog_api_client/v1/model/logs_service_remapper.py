# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsServiceRemapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_service_remapper_type import LogsServiceRemapperType

        return {
            "is_enabled": (bool,),
            "name": (str,),
            "sources": ([str],),
            "type": (LogsServiceRemapperType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "name": "name",
        "sources": "sources",
        "type": "type",
    }

    def __init__(self, sources, type, *args, **kwargs):
        """
        Use this processor if you want to assign one or more attributes as the official service.

        **Note:** If multiple service remapper processors can be applied to a given log,
        only the first one (according to the pipeline order) is taken into account.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param sources: Array of source attributes.
        :type sources: [str]

        :param type: Type of logs service remapper.
        :type type: LogsServiceRemapperType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.type = type

    @classmethod
    def _from_openapi_data(cls, sources, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsServiceRemapper, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.type = type
        return self
