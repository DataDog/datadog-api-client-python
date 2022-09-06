# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FormulaAndFunctionMetricQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_metric_aggregation import (
            FormulaAndFunctionMetricAggregation,
        )
        from datadog_api_client.v1.model.formula_and_function_metric_data_source import (
            FormulaAndFunctionMetricDataSource,
        )

        return {
            "aggregator": (FormulaAndFunctionMetricAggregation,),
            "data_source": (FormulaAndFunctionMetricDataSource,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(self_, data_source, name, query, *args, **kwargs):
        """
        A formula and functions metrics query.

        :param aggregator: The aggregation methods available for metrics queries.
        :type aggregator: FormulaAndFunctionMetricAggregation, optional

        :param data_source: Data source for metrics queries.
        :type data_source: FormulaAndFunctionMetricDataSource

        :param name: Name of the query for use in formulas.
        :type name: str

        :param query: Metrics query definition.
        :type query: str
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
