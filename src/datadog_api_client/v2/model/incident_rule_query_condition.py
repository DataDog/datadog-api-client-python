# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class IncidentRuleQueryCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "normalized_query": (str, none_type),
            "raw_query": (str, none_type),
        }

    attribute_map = {
        "normalized_query": "normalized_query",
        "raw_query": "raw_query",
    }

    def __init__(
        self_,
        normalized_query: Union[str, none_type, UnsetType] = unset,
        raw_query: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A query-based condition for an incident rule.

        :param normalized_query: The normalized query string.
        :type normalized_query: str, none_type, optional

        :param raw_query: The raw query string.
        :type raw_query: str, none_type, optional
        """
        if normalized_query is not unset:
            kwargs["normalized_query"] = normalized_query
        if raw_query is not unset:
            kwargs["raw_query"] = raw_query
        super().__init__(kwargs)
