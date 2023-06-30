# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
    from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions
    from datadog_api_client.v2.model.spans_list_request_page import SpansListRequestPage
    from datadog_api_client.v2.model.spans_sort import SpansSort


class SpansListRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
        from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions
        from datadog_api_client.v2.model.spans_list_request_page import SpansListRequestPage
        from datadog_api_client.v2.model.spans_sort import SpansSort

        return {
            "filter": (SpansQueryFilter,),
            "options": (SpansQueryOptions,),
            "page": (SpansListRequestPage,),
            "sort": (SpansSort,),
        }

    attribute_map = {
        "filter": "filter",
        "options": "options",
        "page": "page",
        "sort": "sort",
    }

    def __init__(
        self_,
        filter: Union[SpansQueryFilter, UnsetType] = unset,
        options: Union[SpansQueryOptions, UnsetType] = unset,
        page: Union[SpansListRequestPage, UnsetType] = unset,
        sort: Union[SpansSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object containing all the query parameters.

        :param filter: The search and filter query settings.
        :type filter: SpansQueryFilter, optional

        :param options: Global query options that are used during the query.
            Note: You should only supply timezone or time offset but not both otherwise the query will fail.
        :type options: SpansQueryOptions, optional

        :param page: Paging attributes for listing spans.
        :type page: SpansListRequestPage, optional

        :param sort: Sort parameters when querying spans.
        :type sort: SpansSort, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if options is not unset:
            kwargs["options"] = options
        if page is not unset:
            kwargs["page"] = page
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)
