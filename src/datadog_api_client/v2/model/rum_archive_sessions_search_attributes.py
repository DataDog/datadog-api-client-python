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


class RumArchiveSessionsSearchAttributes(ModelNormal):
    validations = {
        "_from": {
            "inclusive_minimum": 1,
        },
        "limit": {
            "inclusive_maximum": 1000,
        },
        "to": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "cursor": (str,),
            "_from": (int,),
            "hide_retained": (bool,),
            "limit": (int,),
            "query": (str,),
            "to": (int,),
        }

    attribute_map = {
        "cursor": "cursor",
        "_from": "from",
        "hide_retained": "hide_retained",
        "limit": "limit",
        "query": "query",
        "to": "to",
    }

    def __init__(
        self_,
        _from: int,
        query: str,
        to: int,
        cursor: Union[str, UnsetType] = unset,
        hide_retained: Union[bool, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Archived-session query. A window wider than configured archive retention is narrowed before searching.

        :param cursor: Opaque next-page cursor. Keep the query, time range, and hide_retained value unchanged.
        :type cursor: str, optional

        :param _from: Start of the range in Unix milliseconds. Must be positive and earlier than to.
        :type _from: int

        :param hide_retained: When true, exclude sessions already present in hot RUM storage. When false, those sessions can appear in the results. Keep this value unchanged when continuing with a cursor.
        :type hide_retained: bool, optional

        :param limit: Page size, at most 1000 (default 50). Values at or below zero use 50.
        :type limit: int, optional

        :param query: RUM search query. Must not be empty.
        :type query: str

        :param to: End of the range in Unix milliseconds.
        :type to: int
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if hide_retained is not unset:
            kwargs["hide_retained"] = hide_retained
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
