# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.derived_metric_query import DerivedMetricQuery


class DerivedMetricDefinition(ModelNormal):
    validations = {
        "queries": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.derived_metric_query import DerivedMetricQuery

        return {
            "formula": (str,),
            "queries": ([DerivedMetricQuery],),
        }

    attribute_map = {
        "formula": "formula",
        "queries": "queries",
    }

    def __init__(self_, formula: str, queries: List[DerivedMetricQuery], **kwargs):
        """
        The definition of a derived metric as a formula over one or more queries.

        :param formula: The formula that combines the queries into the value of the derived metric.
        :type formula: str

        :param queries: The list of queries referenced by the formula.
        :type queries: [DerivedMetricQuery]
        """
        super().__init__(kwargs)

        self_.formula = formula
        self_.queries = queries
