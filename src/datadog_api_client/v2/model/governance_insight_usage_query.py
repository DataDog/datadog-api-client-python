# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GovernanceInsightUsageQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
            "reducer": (str,),
        }

    attribute_map = {
        "query": "query",
        "reducer": "reducer",
    }

    def __init__(self_, query: str, reducer: str, **kwargs):
        """
        A usage query used to compute an insight value.

        :param query: The usage query string.
        :type query: str

        :param reducer: How the query result series is reduced to a single value.
        :type reducer: str
        """
        super().__init__(kwargs)

        self_.query = query
        self_.reducer = reducer
