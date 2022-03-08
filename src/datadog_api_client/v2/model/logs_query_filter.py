# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsQueryFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (str,),
            "indexes": ([str],),
            "query": (str,),
            "to": (str,),
        }

    attribute_map = {
        "_from": "from",
        "indexes": "indexes",
        "query": "query",
        "to": "to",
    }

    def __init__(self, *args, **kwargs):
        """
        The search and filter query settings

        :param _from: The minimum time for the requested logs, supports date math and regular timestamps (milliseconds).
        :type _from: str, optional

        :param indexes: For customers with multiple indexes, the indexes to search. Defaults to ['*'] which means all indexes.
        :type indexes: [str], optional

        :param query: The search query - following the log search syntax.
        :type query: str, optional

        :param to: The maximum time for the requested logs, supports date math and regular timestamps (milliseconds).
        :type to: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsQueryFilter, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
