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


class SLOTimeSliceQuery(ModelNormal):
    validations = {
        "formulas": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_formula import SLOFormula
        from datadog_api_client.v1.model.slo_data_source_query_definition import SLODataSourceQueryDefinition

        return {
            "formulas": ([SLOFormula],),
            "queries": ([SLODataSourceQueryDefinition],),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
    }

    def __init__(
        self_,
        formulas: List[SLOFormula],
        queries: List[Union[SLODataSourceQueryDefinition, FormulaAndFunctionMetricQueryDefinition]],
        **kwargs,
    ):
        """
        The queries and formula used to calculate the SLI value.

        :param formulas: A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.
        :type formulas: [SLOFormula]

        :param queries: A list of queries that are used to calculate the SLI value.
        :type queries: [SLODataSourceQueryDefinition]
        """
        super().__init__(kwargs)

        self_.formulas = formulas
        self_.queries = queries
