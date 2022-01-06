# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.logs_aggregate_request_page import LogsAggregateRequestPage
    from datadog_api_client.v2.model.logs_compute import LogsCompute
    from datadog_api_client.v2.model.logs_group_by import LogsGroupBy
    from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
    from datadog_api_client.v2.model.logs_query_options import LogsQueryOptions

    globals()["LogsAggregateRequestPage"] = LogsAggregateRequestPage
    globals()["LogsCompute"] = LogsCompute
    globals()["LogsGroupBy"] = LogsGroupBy
    globals()["LogsQueryFilter"] = LogsQueryFilter
    globals()["LogsQueryOptions"] = LogsQueryOptions


class LogsAggregateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
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

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """LogsAggregateRequest - a model defined in OpenAPI

        Keyword Args:
            compute ([LogsCompute]): [optional] The list of metrics or timeseries to compute for the retrieved buckets.
            filter (LogsQueryFilter): [optional]
            group_by ([LogsGroupBy]): [optional] The rules for the group by
            options (LogsQueryOptions): [optional]
            page (LogsAggregateRequestPage): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAggregateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
