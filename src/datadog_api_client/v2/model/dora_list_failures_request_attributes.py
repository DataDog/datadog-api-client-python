# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class DORAListFailuresRequestAttributes(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "_from": (datetime,),
            "limit": (int,),
            "query": (str,),
            "sort": (str,),
            "to": (datetime,),
        }

    attribute_map = {
        "_from": "from",
        "limit": "limit",
        "query": "query",
        "sort": "sort",
        "to": "to",
    }

    def __init__(
        self_,
        _from: Union[datetime, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        to: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to get a list of failures.

        :param _from: Minimum timestamp for requested events.
        :type _from: datetime, optional

        :param limit: Maximum number of events in the response.
        :type limit: int, optional

        :param query: Search query with event platform syntax.
        :type query: str, optional

        :param sort: Sort order (prefixed with ``-`` for descending).
        :type sort: str, optional

        :param to: Maximum timestamp for requested events.
        :type to: datetime, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if limit is not unset:
            kwargs["limit"] = limit
        if query is not unset:
            kwargs["query"] = query
        if sort is not unset:
            kwargs["sort"] = sort
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)
