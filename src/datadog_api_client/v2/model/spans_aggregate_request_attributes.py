# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_compute import SpansCompute
    from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
    from datadog_api_client.v2.model.spans_group_by import SpansGroupBy
    from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions


class SpansAggregateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_compute import SpansCompute
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
        from datadog_api_client.v2.model.spans_group_by import SpansGroupBy
        from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions

        return {
            "compute": ([SpansCompute],),
            "filter": (SpansQueryFilter,),
            "group_by": ([SpansGroupBy],),
            "options": (SpansQueryOptions,),
        }

    attribute_map = {
        "compute": "compute",
        "filter": "filter",
        "group_by": "group_by",
        "options": "options",
    }

    def __init__(
        self_,
        compute: Union[List[SpansCompute], UnsetType] = unset,
        filter: Union[SpansQueryFilter, UnsetType] = unset,
        group_by: Union[List[SpansGroupBy], UnsetType] = unset,
        options: Union[SpansQueryOptions, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object containing all the query parameters.

        :param compute: The list of metrics or timeseries to compute for the retrieved buckets.
        :type compute: [SpansCompute], optional

        :param filter: The search and filter query settings.
        :type filter: SpansQueryFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [SpansGroupBy], optional

        :param options: Global query options that are used during the query.
            Note: You should only supply timezone or time offset but not both otherwise the query will fail.
        :type options: SpansQueryOptions, optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if options is not unset:
            kwargs["options"] = options
        super().__init__(kwargs)
