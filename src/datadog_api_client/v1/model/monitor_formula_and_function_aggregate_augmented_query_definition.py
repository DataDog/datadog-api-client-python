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
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_augment_query import (
        MonitorFormulaAndFunctionAggregateAugmentQuery,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_base_query import (
        MonitorFormulaAndFunctionAggregateBaseQuery,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
        MonitorFormulaAndFunctionEventQueryDefinitionCompute,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_augmented_data_source import (
        MonitorFormulaAndFunctionAggregateAugmentedDataSource,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by import (
        MonitorFormulaAndFunctionEventQueryGroupBy,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_join_condition import (
        MonitorFormulaAndFunctionAggregateQueryJoinCondition,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition import (
        MonitorFormulaAndFunctionEventQueryDefinition,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_query_definition import (
        MonitorFormulaAndFunctionReferenceTableQueryDefinition,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_metrics_query_definition import (
        MonitorFormulaAndFunctionMetricsQueryDefinition,
    )


class MonitorFormulaAndFunctionAggregateAugmentedQueryDefinition(ModelNormal):
    validations = {
        "compute": {
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_augment_query import (
            MonitorFormulaAndFunctionAggregateAugmentQuery,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_base_query import (
            MonitorFormulaAndFunctionAggregateBaseQuery,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
            MonitorFormulaAndFunctionEventQueryDefinitionCompute,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_augmented_data_source import (
            MonitorFormulaAndFunctionAggregateAugmentedDataSource,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by import (
            MonitorFormulaAndFunctionEventQueryGroupBy,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_join_condition import (
            MonitorFormulaAndFunctionAggregateQueryJoinCondition,
        )

        return {
            "augment_query": (MonitorFormulaAndFunctionAggregateAugmentQuery,),
            "base_query": (MonitorFormulaAndFunctionAggregateBaseQuery,),
            "compute": ([MonitorFormulaAndFunctionEventQueryDefinitionCompute],),
            "data_source": (MonitorFormulaAndFunctionAggregateAugmentedDataSource,),
            "group_by": ([MonitorFormulaAndFunctionEventQueryGroupBy],),
            "join_condition": (MonitorFormulaAndFunctionAggregateQueryJoinCondition,),
            "name": (str,),
        }

    attribute_map = {
        "augment_query": "augment_query",
        "base_query": "base_query",
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "join_condition": "join_condition",
        "name": "name",
    }

    def __init__(
        self_,
        augment_query: Union[
            MonitorFormulaAndFunctionAggregateAugmentQuery,
            MonitorFormulaAndFunctionEventQueryDefinition,
            MonitorFormulaAndFunctionReferenceTableQueryDefinition,
        ],
        base_query: Union[
            MonitorFormulaAndFunctionAggregateBaseQuery,
            MonitorFormulaAndFunctionEventQueryDefinition,
            MonitorFormulaAndFunctionMetricsQueryDefinition,
        ],
        compute: List[MonitorFormulaAndFunctionEventQueryDefinitionCompute],
        data_source: MonitorFormulaAndFunctionAggregateAugmentedDataSource,
        group_by: List[MonitorFormulaAndFunctionEventQueryGroupBy],
        join_condition: MonitorFormulaAndFunctionAggregateQueryJoinCondition,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions aggregate augmented query. Used to enrich base query results with data from a reference table.

        :param augment_query: Augment query for aggregate augmented queries. Can be an events query or a reference table query.
        :type augment_query: MonitorFormulaAndFunctionAggregateAugmentQuery

        :param base_query: Base query for aggregate queries. Can be an events query or a metrics query.
        :type base_query: MonitorFormulaAndFunctionAggregateBaseQuery

        :param compute: Compute options for the query.
        :type compute: [MonitorFormulaAndFunctionEventQueryDefinitionCompute]

        :param data_source: Data source for aggregate augmented queries.
        :type data_source: MonitorFormulaAndFunctionAggregateAugmentedDataSource

        :param group_by: Group by options for the query.
        :type group_by: [MonitorFormulaAndFunctionEventQueryGroupBy]

        :param join_condition: Join condition for aggregate augmented queries.
        :type join_condition: MonitorFormulaAndFunctionAggregateQueryJoinCondition

        :param name: Name of the query for use in formulas.
        :type name: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.augment_query = augment_query
        self_.base_query = base_query
        self_.compute = compute
        self_.data_source = data_source
        self_.group_by = group_by
        self_.join_condition = join_condition
