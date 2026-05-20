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
    from datadog_api_client.v2.model.llm_obs_span_filter import LLMObsSpanFilter
    from datadog_api_client.v2.model.llm_obs_span_search_options import LLMObsSpanSearchOptions
    from datadog_api_client.v2.model.llm_obs_span_page_query import LLMObsSpanPageQuery


class LLMObsSearchSpansRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_span_filter import LLMObsSpanFilter
        from datadog_api_client.v2.model.llm_obs_span_search_options import LLMObsSpanSearchOptions
        from datadog_api_client.v2.model.llm_obs_span_page_query import LLMObsSpanPageQuery

        return {
            "filter": (LLMObsSpanFilter,),
            "options": (LLMObsSpanSearchOptions,),
            "page": (LLMObsSpanPageQuery,),
            "sort": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "options": "options",
        "page": "page",
        "sort": "sort",
    }

    def __init__(
        self_,
        filter: Union[LLMObsSpanFilter, UnsetType] = unset,
        options: Union[LLMObsSpanSearchOptions, UnsetType] = unset,
        page: Union[LLMObsSpanPageQuery, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability spans search request.

        :param filter: Filter criteria for an LLM Observability span search.
        :type filter: LLMObsSpanFilter, optional

        :param options: Additional options for a span search request.
        :type options: LLMObsSpanSearchOptions, optional

        :param page: Pagination settings for a span search request.
        :type page: LLMObsSpanPageQuery, optional

        :param sort: Sort order for the results. Use ``-`` prefix for descending order.
        :type sort: str, optional
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
