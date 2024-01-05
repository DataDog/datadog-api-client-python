# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityMonitoringThirdPartyRootQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "group_by_fields": ([str],),
            "query": (str,),
        }

    attribute_map = {
        "group_by_fields": "groupByFields",
        "query": "query",
    }

    def __init__(
        self_, group_by_fields: Union[List[str], UnsetType] = unset, query: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        A query to be combined with the third party case query.

        :param group_by_fields: Fields to group by.
        :type group_by_fields: [str], optional

        :param query: Query to run on logs.
        :type query: str, optional
        """
        if group_by_fields is not unset:
            kwargs["group_by_fields"] = group_by_fields
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
