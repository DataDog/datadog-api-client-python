# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsAggregateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_compute import LogsCompute
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_group_by import LogsGroupBy
        from datadog_api_client.v2.model.logs_query_options import LogsQueryOptions
        from datadog_api_client.v2.model.logs_aggregate_request_page import LogsAggregateRequestPage

        return {
            "compute": ([LogsCompute],),
            "filter": (LogsQueryFilter,),
            "group_by": ([LogsGroupBy],),
            "options": (LogsQueryOptions,),
            "page": (LogsAggregateRequestPage,),
        }

    attribute_map = {
        "compute": "compute",
        "filter": "filter",
        "group_by": "group_by",
        "options": "options",
        "page": "page",
    }

    def __init__(self, *args, **kwargs):
        """
        The object sent with the request to retrieve a list of logs from your organization.

        :param compute: The list of metrics or timeseries to compute for the retrieved buckets.
        :type compute: [LogsCompute], optional

        :param filter: The search and filter query settings
        :type filter: LogsQueryFilter, optional

        :param group_by: The rules for the group by
        :type group_by: [LogsGroupBy], optional

        :param options: Global query options that are used during the query.
            Note: You should only supply timezone or time offset but not both otherwise the query will fail.
        :type options: LogsQueryOptions, optional

        :param page: Paging settings
        :type page: LogsAggregateRequestPage, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAggregateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
