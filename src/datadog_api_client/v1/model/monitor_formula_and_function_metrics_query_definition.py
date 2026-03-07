# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.monitor_formula_and_function_metrics_aggregator import (
        MonitorFormulaAndFunctionMetricsAggregator,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_metrics_data_source import (
        MonitorFormulaAndFunctionMetricsDataSource,
    )


class MonitorFormulaAndFunctionMetricsQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_metrics_aggregator import (
            MonitorFormulaAndFunctionMetricsAggregator,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_metrics_data_source import (
            MonitorFormulaAndFunctionMetricsDataSource,
        )

        return {
            "aggregator": (MonitorFormulaAndFunctionMetricsAggregator,),
            "data_source": (MonitorFormulaAndFunctionMetricsDataSource,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        data_source: MonitorFormulaAndFunctionMetricsDataSource,
        query: str,
        aggregator: Union[MonitorFormulaAndFunctionMetricsAggregator, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions metrics query for use in aggregate queries.

        :param aggregator: Aggregator for metrics queries.
        :type aggregator: MonitorFormulaAndFunctionMetricsAggregator, optional

        :param data_source: Data source for metrics queries.
        :type data_source: MonitorFormulaAndFunctionMetricsDataSource

        :param name: Name of the query for use in formulas.
        :type name: str, optional

        :param query: The metrics query definition.
        :type query: str
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query = query
