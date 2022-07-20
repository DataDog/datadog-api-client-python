# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_query_compute import LogsQueryCompute
        from datadog_api_client.v1.model.log_query_definition_group_by import LogQueryDefinitionGroupBy
        from datadog_api_client.v1.model.log_query_definition_search import LogQueryDefinitionSearch

        return {
            "compute": (LogsQueryCompute,),
            "group_by": ([LogQueryDefinitionGroupBy],),
            "index": (str,),
            "multi_compute": ([LogsQueryCompute],),
            "search": (LogQueryDefinitionSearch,),
        }

    attribute_map = {
        "compute": "compute",
        "group_by": "group_by",
        "index": "index",
        "multi_compute": "multi_compute",
        "search": "search",
    }

    def __init__(self, *args, **kwargs):
        """
        The log query.

        :param compute: Define computation for a log query.
        :type compute: LogsQueryCompute, optional

        :param group_by: List of tag prefixes to group by in the case of a cluster check.
        :type group_by: [LogQueryDefinitionGroupBy], optional

        :param index: A coma separated-list of index names. Use "*" query all indexes at once. `Multiple Indexes <https://docs.datadoghq.com/logs/indexes/#multiple-indexes>`_
        :type index: str, optional

        :param multi_compute: This field is mutually exclusive with ``compute``.
        :type multi_compute: [LogsQueryCompute], optional

        :param search: The query being made on the logs.
        :type search: LogQueryDefinitionSearch, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
