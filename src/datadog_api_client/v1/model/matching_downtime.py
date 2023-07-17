# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class MatchingDowntime(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (int, none_type),
            "id": (int,),
            "scope": ([str],),
            "start": (int,),
        }

    attribute_map = {
        "end": "end",
        "id": "id",
        "scope": "scope",
        "start": "start",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_,
        id: int,
        end: Union[int, none_type, UnsetType] = unset,
        scope: Union[List[str], UnsetType] = unset,
        start: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing a downtime that matches this monitor.

        :param end: POSIX timestamp to end the downtime.
        :type end: int, none_type, optional

        :param id: The downtime ID.
        :type id: int

        :param scope: The scope(s) to which the downtime applies. Must be in ``key:value`` format. For example, ``host:app2``.
            Provide multiple scopes as a comma-separated list like ``env:dev,env:prod``.
            The resulting downtime applies to sources that matches ALL provided scopes ( ``env:dev`` **AND** ``env:prod`` ).
        :type scope: [str], optional

        :param start: POSIX timestamp to start the downtime.
        :type start: int, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if scope is not unset:
            kwargs["scope"] = scope
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)

        self_.id = id
