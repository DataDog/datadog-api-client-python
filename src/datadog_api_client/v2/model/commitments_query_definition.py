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
    from datadog_api_client.v2.model.commitments_query_definition_formula import CommitmentsQueryDefinitionFormula
    from datadog_api_client.v2.model.commitments_query_definition_query import CommitmentsQueryDefinitionQuery


class CommitmentsQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_query_definition_formula import CommitmentsQueryDefinitionFormula
        from datadog_api_client.v2.model.commitments_query_definition_query import CommitmentsQueryDefinitionQuery

        return {
            "formulas": ([CommitmentsQueryDefinitionFormula],),
            "queries": ([CommitmentsQueryDefinitionQuery],),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
    }

    def __init__(
        self_,
        formulas: List[CommitmentsQueryDefinitionFormula],
        queries: List[CommitmentsQueryDefinitionQuery],
        **kwargs,
    ):
        """
        The query that produces the response values, in the same format as dashboard and notebook widget
        requests, so a client can graph the values in a widget. Each formula's ``id`` names the response value
        that it produces.

        :param formulas: The formulas of a query definition.
        :type formulas: [CommitmentsQueryDefinitionFormula]

        :param queries: The metric queries of a query definition.
        :type queries: [CommitmentsQueryDefinitionQuery]
        """
        super().__init__(kwargs)

        self_.formulas = formulas
        self_.queries = queries
