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
    from datadog_api_client.v2.model.sankey_request_data_attributes_search_audience_filters import (
        SankeyRequestDataAttributesSearchAudienceFilters,
    )
    from datadog_api_client.v2.model.sankey_request_data_attributes_search_occurrences import (
        SankeyRequestDataAttributesSearchOccurrences,
    )


class SankeyRequestDataAttributesSearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sankey_request_data_attributes_search_audience_filters import (
            SankeyRequestDataAttributesSearchAudienceFilters,
        )
        from datadog_api_client.v2.model.sankey_request_data_attributes_search_occurrences import (
            SankeyRequestDataAttributesSearchOccurrences,
        )

        return {
            "audience_filters": (SankeyRequestDataAttributesSearchAudienceFilters,),
            "occurrences": (SankeyRequestDataAttributesSearchOccurrences,),
            "query": (str,),
            "subquery_id": (str,),
        }

    attribute_map = {
        "audience_filters": "audience_filters",
        "occurrences": "occurrences",
        "query": "query",
        "subquery_id": "subquery_id",
    }

    def __init__(
        self_,
        audience_filters: Union[SankeyRequestDataAttributesSearchAudienceFilters, UnsetType] = unset,
        occurrences: Union[SankeyRequestDataAttributesSearchOccurrences, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        subquery_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param audience_filters:
        :type audience_filters: SankeyRequestDataAttributesSearchAudienceFilters, optional

        :param occurrences:
        :type occurrences: SankeyRequestDataAttributesSearchOccurrences, optional

        :param query:
        :type query: str, optional

        :param subquery_id:
        :type subquery_id: str, optional
        """
        if audience_filters is not unset:
            kwargs["audience_filters"] = audience_filters
        if occurrences is not unset:
            kwargs["occurrences"] = occurrences
        if query is not unset:
            kwargs["query"] = query
        if subquery_id is not unset:
            kwargs["subquery_id"] = subquery_id
        super().__init__(kwargs)
