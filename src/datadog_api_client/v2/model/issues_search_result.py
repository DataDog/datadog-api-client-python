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
    from datadog_api_client.v2.model.issues_search_result_attributes import IssuesSearchResultAttributes
    from datadog_api_client.v2.model.issues_search_result_relationships import IssuesSearchResultRelationships
    from datadog_api_client.v2.model.issues_search_result_type import IssuesSearchResultType


class IssuesSearchResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issues_search_result_attributes import IssuesSearchResultAttributes
        from datadog_api_client.v2.model.issues_search_result_relationships import IssuesSearchResultRelationships
        from datadog_api_client.v2.model.issues_search_result_type import IssuesSearchResultType

        return {
            "attributes": (IssuesSearchResultAttributes,),
            "id": (str,),
            "relationships": (IssuesSearchResultRelationships,),
            "type": (IssuesSearchResultType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IssuesSearchResultAttributes,
        id: str,
        type: IssuesSearchResultType,
        relationships: Union[IssuesSearchResultRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Result matching the search query.

        :param attributes: Object containing the information of a search result.
        :type attributes: IssuesSearchResultAttributes

        :param id: Search result identifier (matches the nested issue's identifier).
        :type id: str

        :param relationships: Relationships between the search result and other resources.
        :type relationships: IssuesSearchResultRelationships, optional

        :param type: Type of the object.
        :type type: IssuesSearchResultType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
