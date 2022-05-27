# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsPipeline(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_filter import LogsFilter
        from datadog_api_client.v1.model.logs_processor import LogsProcessor

        return {
            "filter": (LogsFilter,),
            "id": (str,),
            "is_enabled": (bool,),
            "is_read_only": (bool,),
            "name": (str,),
            "processors": ([LogsProcessor],),
            "type": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "id": "id",
        "is_enabled": "is_enabled",
        "is_read_only": "is_read_only",
        "name": "name",
        "processors": "processors",
        "type": "type",
    }
    read_only_vars = {
        "id",
        "is_read_only",
        "type",
    }

    def __init__(self, name, *args, **kwargs):
        """
        Pipelines and processors operate on incoming logs,
        parsing and transforming them into structured attributes for easier querying.

        **Note** : These endpoints are only available for admin users.
        Make sure to use an application key created by an admin.

        :param filter: Filter for logs.
        :type filter: LogsFilter, optional

        :param id: ID of the pipeline.
        :type id: str, optional

        :param is_enabled: Whether or not the pipeline is enabled.
        :type is_enabled: bool, optional

        :param is_read_only: Whether or not the pipeline can be edited.
        :type is_read_only: bool, optional

        :param name: Name of the pipeline.
        :type name: str

        :param processors: Ordered list of processors in this pipeline.
        :type processors: [LogsProcessor], optional

        :param type: Type of pipeline.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name

    @classmethod
    def _from_openapi_data(cls, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsPipeline, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        return self
