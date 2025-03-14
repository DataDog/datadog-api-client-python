# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumMetricFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
        }

    attribute_map = {
        "query": "query",
    }

    def __init__(self_, **kwargs):
        """
        The rum-based metric filter. Events matching this filter will be aggregated in this metric.

        :param query: The search query - following the RUM search syntax.
        :type query: str
        """
        super().__init__(kwargs)
        query = kwargs.get("query", "*")

        self_.query = query
