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
    from datadog_api_client.v2.model.unit_cost_formula import UnitCostFormula
    from datadog_api_client.v2.model.unit_cost_query import UnitCostQuery


class UnitCostQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit_cost_formula import UnitCostFormula
        from datadog_api_client.v2.model.unit_cost_query import UnitCostQuery

        return {
            "formulas": ([UnitCostFormula],),
            "queries": ([UnitCostQuery],),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
    }

    def __init__(self_, formulas: List[UnitCostFormula], queries: List[UnitCostQuery], **kwargs):
        """
        A timeseries object containing ``queries`` and ``formulas`` arrays.

        :param formulas: The list of formulas applied to the queries for this side of the ratio.
        :type formulas: [UnitCostFormula]

        :param queries: The list of queries evaluated for this side of the ratio.
        :type queries: [UnitCostQuery]
        """
        super().__init__(kwargs)

        self_.formulas = formulas
        self_.queries = queries
