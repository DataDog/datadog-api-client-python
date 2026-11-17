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


class SegmentEventPlatformBlock(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "facet": (str,),
            "_from": (str,),
            "name": (str,),
            "query": (str,),
            "to": (str,),
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
        _from: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        to: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Selects the users or accounts that sent matching RUM or Product Analytics events in a time range.
        ``from`` and ``to`` are epoch milliseconds, or negative offsets in milliseconds relative to now. ``0`` means now.

        :param facet: Facet that identifies the entity, such as ``@usr.id``.
        :type facet: str

        :param _from: Start of the time range.
        :type _from: str, optional

        :param name: Name of the block, used in ``combination``.
        :type name: str, optional

        :param query: Event search query.
        :type query: str, optional

        :param to: End of the time range.
        :type to: str, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)

        self_.facet = facet
