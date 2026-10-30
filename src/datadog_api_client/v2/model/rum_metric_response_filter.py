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


class RumMetricResponseFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
        }

    attribute_map = {
        "query": "query",
    }

    def __init__(self_, query: Union[str, UnsetType] = unset, **kwargs):
        """
        The RUM-based metric filter. RUM events matching this filter are aggregated in this metric. Omitted if the metric only filters on the event type.

        :param query: The search query, following the `RUM search syntax <https://docs.datadoghq.com/real_user_monitoring/explorer/search_syntax/>`_. It does not include the event type filter.
        :type query: str, optional
        """
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
