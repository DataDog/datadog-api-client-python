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


class ProductAnalyticsAudienceUserSubquery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "name": "name",
        "query": "query",
    }

    def __init__(self_, name: str, query: Union[str, UnsetType] = unset, **kwargs):
        """
        A user-based audience query.

        :param name: Name of this query, referenced in the formula.
        :type name: str

        :param query: Search query for filtering users.
        :type query: str, optional
        """
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)

        self_.name = name
