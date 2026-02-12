# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.slo_formula import SLOFormula
    from datadog_api_client.v1.model.slo_data_source_query_definition import SLODataSourceQueryDefinition
    from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
        FormulaAndFunctionMetricQueryDefinition,
    )


class SLOCountDefinition(ModelNormal):
    validations = {
        "queries": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_formula import SLOFormula
        from datadog_api_client.v1.model.slo_data_source_query_definition import SLODataSourceQueryDefinition

        return {
            "good_events_formula": (SLOFormula,),
            "queries": ([SLODataSourceQueryDefinition],),
            "total_events_formula": (SLOFormula,),
        }

    attribute_map = {
        "good_events_formula": "good_events_formula",
        "queries": "queries",
        "total_events_formula": "total_events_formula",
    }

    def __init__(
        self_,
        good_events_formula: SLOFormula,
        queries: List[Union[SLODataSourceQueryDefinition, FormulaAndFunctionMetricQueryDefinition]],
        total_events_formula: SLOFormula,
        **kwargs,
    ):
        """
        A count-based (metric) SLI specification, composed of three parts: the good events formula, the total events formula,
        and the underlying queries.

        :param good_events_formula: A formula that specifies how to combine the results of multiple queries.
        :type good_events_formula: SLOFormula

        :param queries:
        :type queries: [SLODataSourceQueryDefinition]

        :param total_events_formula: A formula that specifies how to combine the results of multiple queries.
        :type total_events_formula: SLOFormula
        """
        super().__init__(kwargs)

        self_.good_events_formula = good_events_formula
        self_.queries = queries
        self_.total_events_formula = total_events_formula
