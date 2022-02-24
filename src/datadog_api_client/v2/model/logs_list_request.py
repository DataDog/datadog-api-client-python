# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
    from datadog_api_client.v2.model.logs_query_options import LogsQueryOptions
    from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
    from datadog_api_client.v2.model.logs_sort import LogsSort

    globals()["LogsQueryFilter"] = LogsQueryFilter
    globals()["LogsQueryOptions"] = LogsQueryOptions
    globals()["LogsListRequestPage"] = LogsListRequestPage
    globals()["LogsSort"] = LogsSort


class LogsListRequest(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "filter": (LogsQueryFilter,),
            "options": (LogsQueryOptions,),
            "page": (LogsListRequestPage,),
            "sort": (LogsSort,),
        }

    attribute_map = {
        "filter": "filter",
        "options": "options",
        "page": "page",
        "sort": "sort",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        The request for a logs list.

        :param filter: The search and filter query settings
        :type filter: LogsQueryFilter, optional

        :param options: Global query options that are used during the query.
            Note: You should only supply timezone or time offset but not both otherwise the query will fail.
        :type options: LogsQueryOptions, optional

        :param page: Paging attributes for listing logs.
        :type page: LogsListRequestPage, optional

        :param sort: Sort parameters when querying logs.
        :type sort: LogsSort, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsListRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
