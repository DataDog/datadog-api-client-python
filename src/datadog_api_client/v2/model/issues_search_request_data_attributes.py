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
    from datadog_api_client.v2.model.issues_search_request_data_attributes_order_by import (
        IssuesSearchRequestDataAttributesOrderBy,
    )
    from datadog_api_client.v2.model.issues_search_request_data_attributes_persona import (
        IssuesSearchRequestDataAttributesPersona,
    )
    from datadog_api_client.v2.model.issues_search_request_data_attributes_track import (
        IssuesSearchRequestDataAttributesTrack,
    )


class IssuesSearchRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issues_search_request_data_attributes_order_by import (
            IssuesSearchRequestDataAttributesOrderBy,
        )
        from datadog_api_client.v2.model.issues_search_request_data_attributes_persona import (
            IssuesSearchRequestDataAttributesPersona,
        )
        from datadog_api_client.v2.model.issues_search_request_data_attributes_track import (
            IssuesSearchRequestDataAttributesTrack,
        )

        return {
            "_from": (int,),
            "order_by": (IssuesSearchRequestDataAttributesOrderBy,),
            "persona": (IssuesSearchRequestDataAttributesPersona,),
            "query": (str,),
            "to": (int,),
            "track": (IssuesSearchRequestDataAttributesTrack,),
        }

    attribute_map = {
        "_from": "from",
        "order_by": "order_by",
        "persona": "persona",
        "query": "query",
        "to": "to",
        "track": "track",
    }

    def __init__(
        self_,
        _from: int,
        query: str,
        to: int,
        order_by: Union[IssuesSearchRequestDataAttributesOrderBy, UnsetType] = unset,
        persona: Union[IssuesSearchRequestDataAttributesPersona, UnsetType] = unset,
        track: Union[IssuesSearchRequestDataAttributesTrack, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing a search issue request.

        :param _from: Start date (inclusive) of the query in milliseconds since the Unix epoch.
        :type _from: int

        :param order_by: The attribute to sort the search results by.
        :type order_by: IssuesSearchRequestDataAttributesOrderBy, optional

        :param persona: Persona for the search. Either track(s) or persona(s) must be specified.
        :type persona: IssuesSearchRequestDataAttributesPersona, optional

        :param query: Search query following the event search syntax.
        :type query: str

        :param to: End date (exclusive) of the query in milliseconds since the Unix epoch.
        :type to: int

        :param track: Track of the events to query. Either track(s) or persona(s) must be specified.
        :type track: IssuesSearchRequestDataAttributesTrack, optional
        """
        if order_by is not unset:
            kwargs["order_by"] = order_by
        if persona is not unset:
            kwargs["persona"] = persona
        if track is not unset:
            kwargs["track"] = track
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
