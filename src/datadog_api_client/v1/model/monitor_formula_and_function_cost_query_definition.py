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
    from datadog_api_client.v1.model.monitor_formula_and_function_cost_aggregator import (
        MonitorFormulaAndFunctionCostAggregator,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_cost_data_source import (
        MonitorFormulaAndFunctionCostDataSource,
    )


class MonitorFormulaAndFunctionCostQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_cost_aggregator import (
            MonitorFormulaAndFunctionCostAggregator,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_cost_data_source import (
            MonitorFormulaAndFunctionCostDataSource,
        )

        return {
            "aggregator": (MonitorFormulaAndFunctionCostAggregator,),
            "data_source": (MonitorFormulaAndFunctionCostDataSource,),
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
        data_source: MonitorFormulaAndFunctionCostDataSource,
        name: str,
        query: str,
        aggregator: Union[MonitorFormulaAndFunctionCostAggregator, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions cost query.

        :param aggregator: Aggregation methods for metric queries.
        :type aggregator: MonitorFormulaAndFunctionCostAggregator, optional

        :param data_source: Data source for cost queries.
        :type data_source: MonitorFormulaAndFunctionCostDataSource

        :param name: Name of the query for use in formulas.
        :type name: str

        :param query: The monitor query.
        :type query: str
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
