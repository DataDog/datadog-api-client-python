# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class MonitorDowntimeMatchResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (datetime, none_type),
            "groups": ([str],),
            "scope": (str,),
            "start": (datetime,),
        }

    attribute_map = {
        "end": "end",
        "groups": "groups",
        "scope": "scope",
        "start": "start",
    }

    def __init__(
        self_,
        end: Union[datetime, none_type, UnsetType] = unset,
        groups: Union[List[str], UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        start: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Downtime match details.

        :param end: The end of the downtime.
        :type end: datetime, none_type, optional

        :param groups: An array of groups associated with the downtime.
        :type groups: [str], optional

        :param scope: The scope to which the downtime applies. Must follow the `common search syntax <https://docs.datadoghq.com/logs/explorer/search_syntax/>`_.
        :type scope: str, optional

        :param start: The start of the downtime.
        :type start: datetime, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if groups is not unset:
            kwargs["groups"] = groups
        if scope is not unset:
            kwargs["scope"] = scope
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)
