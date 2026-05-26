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
    from datadog_api_client.v2.model.recommendations_filter_request_sort_items import (
        RecommendationsFilterRequestSortItems,
    )


class RecommendationsFilterRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.recommendations_filter_request_sort_items import (
            RecommendationsFilterRequestSortItems,
        )

        return {
            "filter": (str,),
            "scope": (str,),
            "sort": ([RecommendationsFilterRequestSortItems],),
            "view": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "scope": "scope",
        "sort": "sort",
        "view": "view",
    }

    def __init__(
        self_,
        filter: Union[str, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        sort: Union[List[RecommendationsFilterRequestSortItems], UnsetType] = unset,
        view: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request body for filtering cost recommendations.

        :param filter: Filter expression applied to the recommendations.
        :type filter: str, optional

        :param scope: Recommendations scope. Defaults to ``ccm`` ; use ``experiment`` for experimental recommendations or ``*`` for both.
        :type scope: str, optional

        :param sort: Ordered list of sort clauses applied to the result set.
        :type sort: [RecommendationsFilterRequestSortItems], optional

        :param view: Active view name (for example, ``active`` , ``dismissed`` , ``open`` , ``in-progress`` , or ``completed`` ).
        :type view: str, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if scope is not unset:
            kwargs["scope"] = scope
        if sort is not unset:
            kwargs["sort"] = sort
        if view is not unset:
            kwargs["view"] = view
        super().__init__(kwargs)
