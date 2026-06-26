# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GovernanceLimitQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
            "reducer": (str,),
            "source": (str,),
        }

    attribute_map = {
        "query": "query",
        "reducer": "reducer",
        "source": "source",
    }

    def __init__(self_, query: str, reducer: str, source: str, **kwargs):
        """
        A metric query used to compute usage against a limit.

        :param query: The metric query expression used to compute the limit value.
        :type query: str

        :param reducer: How the query results are aggregated into a single value (for example, sum, max, or avg).
        :type reducer: str

        :param source: The data source used to evaluate the metric query (for example, the metrics or events backend).
        :type source: str
        """
        super().__init__(kwargs)

        self_.query = query
        self_.reducer = reducer
        self_.source = source
