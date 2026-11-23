# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn
    from datadog_api_client.v2.model.commitments_unused_cost_meta import CommitmentsUnusedCostMeta
    from datadog_api_client.v2.model.commitments_utilization_scalar_product_breakdown_entry import (
        CommitmentsUtilizationScalarProductBreakdownEntry,
    )
    from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition


class CommitmentsUtilizationScalarResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn
        from datadog_api_client.v2.model.commitments_unused_cost_meta import CommitmentsUnusedCostMeta
        from datadog_api_client.v2.model.commitments_utilization_scalar_product_breakdown_entry import (
            CommitmentsUtilizationScalarProductBreakdownEntry,
        )
        from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition

        return {
            "columns": ([CommitmentsScalarColumn],),
            "meta": (CommitmentsUnusedCostMeta,),
            "product_breakdown": ([CommitmentsUtilizationScalarProductBreakdownEntry],),
            "query_definition": (CommitmentsQueryDefinition,),
        }

    attribute_map = {
        "columns": "columns",
        "meta": "meta",
        "product_breakdown": "product_breakdown",
        "query_definition": "query_definition",
    }

    def __init__(
        self_,
        columns: List[CommitmentsScalarColumn],
        meta: Union[CommitmentsUnusedCostMeta, UnsetType] = unset,
        product_breakdown: Union[List[CommitmentsUtilizationScalarProductBreakdownEntry], UnsetType] = unset,
        query_definition: Union[CommitmentsQueryDefinition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a scalar utilization response.

        :param columns: Array of scalar columns in the response.
        :type columns: [CommitmentsScalarColumn]

        :param meta: Metadata reporting that the cost data lacks the unused costs of some commitments, as with Azure exports
            scoped below the billing profile. Utilization is then overstated, and realized savings and effective
            savings rate are upper bounds. Omitted when the unused costs are available.
        :type meta: CommitmentsUnusedCostMeta, optional

        :param product_breakdown: Array of per-product utilization breakdown entries.
        :type product_breakdown: [CommitmentsUtilizationScalarProductBreakdownEntry], optional

        :param query_definition: The query that produces the response values, in the same format as dashboard and notebook widget
            requests, so a client can graph the values in a widget. Each formula's ``id`` names the response value
            that it produces.
        :type query_definition: CommitmentsQueryDefinition, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if product_breakdown is not unset:
            kwargs["product_breakdown"] = product_breakdown
        if query_definition is not unset:
            kwargs["query_definition"] = query_definition
        super().__init__(kwargs)

        self_.columns = columns
