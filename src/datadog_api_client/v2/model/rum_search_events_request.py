# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMSearchEventsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_query_filter import RUMQueryFilter
        from datadog_api_client.v2.model.rum_query_options import RUMQueryOptions
        from datadog_api_client.v2.model.rum_query_page_options import RUMQueryPageOptions
        from datadog_api_client.v2.model.rum_sort import RUMSort

        return {
            "filter": (RUMQueryFilter,),
            "options": (RUMQueryOptions,),
            "page": (RUMQueryPageOptions,),
            "sort": (RUMSort,),
        }

    attribute_map = {
        "filter": "filter",
        "options": "options",
        "page": "page",
        "sort": "sort",
    }

    def __init__(self, *args, **kwargs):
        """
        The request for a RUM events list.

        :param filter: The search and filter query settings.
        :type filter: RUMQueryFilter, optional

        :param options: Global query options that are used during the query.
            Note: Only supply timezone or time offset, not both. Otherwise, the query fails.
        :type options: RUMQueryOptions, optional

        :param page: Paging attributes for listing events.
        :type page: RUMQueryPageOptions, optional

        :param sort: Sort parameters when querying events.
        :type sort: RUMSort, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMSearchEventsRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
