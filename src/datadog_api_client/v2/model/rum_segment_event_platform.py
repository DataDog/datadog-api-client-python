# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class RumSegmentEventPlatform(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "facet": (str,),
            "_from": (int,),
            "name": (str,),
            "query": (str,),
            "to": (int,),
        }

    attribute_map = {
        "facet": "facet",
        "_from": "from",
        "name": "name",
        "query": "query",
        "to": "to",
    }

    def __init__(
        self_,
        facet: str,
        name: str,
        query: str,
        _from: Union[int, UnsetType] = unset,
        to: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        An event platform query block within a segment data query.

        :param facet: The facet to extract user identifiers from.
        :type facet: str

        :param _from: The start of the time range in milliseconds since epoch.
        :type _from: int, optional

        :param name: The name of this query block.
        :type name: str

        :param query: The search query for filtering events.
        :type query: str

        :param to: The end of the time range in milliseconds since epoch.
        :type to: int, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)

        self_.facet = facet
        self_.name = name
        self_.query = query
