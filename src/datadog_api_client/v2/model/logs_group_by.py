# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_group_by_histogram import LogsGroupByHistogram
        from datadog_api_client.v2.model.logs_group_by_missing import LogsGroupByMissing
        from datadog_api_client.v2.model.logs_aggregate_sort import LogsAggregateSort
        from datadog_api_client.v2.model.logs_group_by_total import LogsGroupByTotal

        return {
            "facet": (str,),
            "histogram": (LogsGroupByHistogram,),
            "limit": (int,),
            "missing": (LogsGroupByMissing,),
            "sort": (LogsAggregateSort,),
            "total": (LogsGroupByTotal,),
        }

    attribute_map = {
        "facet": "facet",
        "histogram": "histogram",
        "limit": "limit",
        "missing": "missing",
        "sort": "sort",
        "total": "total",
    }

    def __init__(self, facet, *args, **kwargs):
        """
        A group by rule

        :param facet: The name of the facet to use (required)
        :type facet: str

        :param histogram: Used to perform a histogram computation (only for measure facets).
            Note: At most 100 buckets are allowed, the number of buckets is (max - min)/interval.
        :type histogram: LogsGroupByHistogram, optional

        :param limit: The maximum buckets to return for this group by
        :type limit: int, optional

        :param missing: The value to use for logs that don't have the facet used to group by
        :type missing: LogsGroupByMissing, optional

        :param sort: A sort rule
        :type sort: LogsAggregateSort, optional

        :param total: A resulting object to put the given computes in over all the matching records.
        :type total: LogsGroupByTotal, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.facet = facet

    @classmethod
    def _from_openapi_data(cls, facet, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsGroupBy, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.facet = facet
        return self
