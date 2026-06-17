# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_insight_metric_query import GovernanceInsightMetricQuery


class GovernanceInsightPercentageQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_insight_metric_query import GovernanceInsightMetricQuery

        return {
            "denominator_query": (GovernanceInsightMetricQuery,),
            "numerator_query": (GovernanceInsightMetricQuery,),
        }

    attribute_map = {
        "denominator_query": "denominator_query",
        "numerator_query": "numerator_query",
    }

    def __init__(
        self_, denominator_query: GovernanceInsightMetricQuery, numerator_query: GovernanceInsightMetricQuery, **kwargs
    ):
        """
        A percentage query that computes an insight value as a ratio of two metric queries.

        :param denominator_query: A metric query used to compute an insight value.
        :type denominator_query: GovernanceInsightMetricQuery

        :param numerator_query: A metric query used to compute an insight value.
        :type numerator_query: GovernanceInsightMetricQuery
        """
        super().__init__(kwargs)

        self_.denominator_query = denominator_query
        self_.numerator_query = numerator_query
