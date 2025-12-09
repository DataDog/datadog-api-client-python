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
    from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
    from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
    from datadog_api_client.v1.model.formula_and_function_metric_semantic_mode import (
        FormulaAndFunctionMetricSemanticMode,
    )


class FormulaAndFunctionMetricQueryDefinition(ModelNormal):
    validations = {
        "cross_org_uuids": {
            "max_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_metric_aggregation import (
            FormulaAndFunctionMetricAggregation,
        )
        from datadog_api_client.v1.model.formula_and_function_metric_data_source import (
            FormulaAndFunctionMetricDataSource,
        )
        from datadog_api_client.v1.model.formula_and_function_metric_semantic_mode import (
            FormulaAndFunctionMetricSemanticMode,
        )

        return {
            "aggregator": (FormulaAndFunctionMetricAggregation,),
            "cross_org_uuids": ([str],),
            "data_source": (FormulaAndFunctionMetricDataSource,),
            "name": (str,),
            "query": (str,),
            "semantic_mode": (FormulaAndFunctionMetricSemanticMode,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
        "semantic_mode": "semantic_mode",
    }

    def __init__(
        self_,
        data_source: FormulaAndFunctionMetricDataSource,
        name: str,
        query: str,
        aggregator: Union[FormulaAndFunctionMetricAggregation, UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        semantic_mode: Union[FormulaAndFunctionMetricSemanticMode, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions metrics query.

        :param aggregator: The aggregation methods available for metrics queries.
        :type aggregator: FormulaAndFunctionMetricAggregation, optional

        :param cross_org_uuids: The source organization UUID for cross organization queries. Feature in Private Beta.
        :type cross_org_uuids: [str], optional

        :param data_source: Data source for metrics queries.
        :type data_source: FormulaAndFunctionMetricDataSource

        :param name: Name of the query for use in formulas.
        :type name: str

        :param query: Metrics query definition.
        :type query: str

        :param semantic_mode: Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed.
        :type semantic_mode: FormulaAndFunctionMetricSemanticMode, optional
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if semantic_mode is not unset:
            kwargs["semantic_mode"] = semantic_mode
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
