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
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_base_query import (
        MonitorFormulaAndFunctionAggregateBaseQuery,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
        MonitorFormulaAndFunctionEventQueryDefinitionCompute,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_filtered_data_source import (
        MonitorFormulaAndFunctionAggregateFilteredDataSource,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_filter_query import (
        MonitorFormulaAndFunctionAggregateFilterQuery,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_filter import (
        MonitorFormulaAndFunctionAggregateQueryFilter,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by import (
        MonitorFormulaAndFunctionEventQueryGroupBy,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition import (
        MonitorFormulaAndFunctionEventQueryDefinition,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_metrics_query_definition import (
        MonitorFormulaAndFunctionMetricsQueryDefinition,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_reference_table_query_definition import (
        MonitorFormulaAndFunctionReferenceTableQueryDefinition,
    )


class MonitorFormulaAndFunctionAggregateFilteredQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_base_query import (
            MonitorFormulaAndFunctionAggregateBaseQuery,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
            MonitorFormulaAndFunctionEventQueryDefinitionCompute,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_filtered_data_source import (
            MonitorFormulaAndFunctionAggregateFilteredDataSource,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_filter_query import (
            MonitorFormulaAndFunctionAggregateFilterQuery,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_filter import (
            MonitorFormulaAndFunctionAggregateQueryFilter,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_event_query_group_by import (
            MonitorFormulaAndFunctionEventQueryGroupBy,
        )

        return {
            "base_query": (MonitorFormulaAndFunctionAggregateBaseQuery,),
            "compute": ([MonitorFormulaAndFunctionEventQueryDefinitionCompute],),
            "data_source": (MonitorFormulaAndFunctionAggregateFilteredDataSource,),
            "filter_query": (MonitorFormulaAndFunctionAggregateFilterQuery,),
            "filters": ([MonitorFormulaAndFunctionAggregateQueryFilter],),
            "group_by": ([MonitorFormulaAndFunctionEventQueryGroupBy],),
            "name": (str,),
        }

    attribute_map = {
        "base_query": "base_query",
        "compute": "compute",
        "data_source": "data_source",
        "filter_query": "filter_query",
        "filters": "filters",
        "group_by": "group_by",
        "name": "name",
    }

    def __init__(
        self_,
        base_query: Union[
            MonitorFormulaAndFunctionAggregateBaseQuery,
            MonitorFormulaAndFunctionEventQueryDefinition,
            MonitorFormulaAndFunctionMetricsQueryDefinition,
        ],
        data_source: MonitorFormulaAndFunctionAggregateFilteredDataSource,
        filter_query: Union[
            MonitorFormulaAndFunctionAggregateFilterQuery,
            MonitorFormulaAndFunctionEventQueryDefinition,
            MonitorFormulaAndFunctionReferenceTableQueryDefinition,
        ],
        filters: List[MonitorFormulaAndFunctionAggregateQueryFilter],
        compute: Union[List[MonitorFormulaAndFunctionEventQueryDefinitionCompute], UnsetType] = unset,
        group_by: Union[List[MonitorFormulaAndFunctionEventQueryGroupBy], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions aggregate filtered query. Used to filter base query results using data from another source.

        :param base_query: Base query for aggregate queries. Can be an events query or a metrics query.
        :type base_query: MonitorFormulaAndFunctionAggregateBaseQuery

        :param compute: Compute options for the query.
        :type compute: [MonitorFormulaAndFunctionEventQueryDefinitionCompute], optional

        :param data_source: Data source for aggregate filtered queries.
        :type data_source: MonitorFormulaAndFunctionAggregateFilteredDataSource

        :param filter_query: Filter query for aggregate filtered queries. Can be an events query or a reference table query.
        :type filter_query: MonitorFormulaAndFunctionAggregateFilterQuery

        :param filters: Filter conditions for the query.
        :type filters: [MonitorFormulaAndFunctionAggregateQueryFilter]

        :param group_by: Group by options for the query.
        :type group_by: [MonitorFormulaAndFunctionEventQueryGroupBy], optional

        :param name: Name of the query for use in formulas.
        :type name: str, optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.base_query = base_query
        self_.data_source = data_source
        self_.filter_query = filter_query
        self_.filters = filters
