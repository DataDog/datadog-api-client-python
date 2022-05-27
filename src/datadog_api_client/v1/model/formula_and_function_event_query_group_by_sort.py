# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FormulaAndFunctionEventQueryGroupBySort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_event_aggregation import (
            FormulaAndFunctionEventAggregation,
        )
        from datadog_api_client.v1.model.query_sort_order import QuerySortOrder

        return {
            "aggregation": (FormulaAndFunctionEventAggregation,),
            "metric": (str,),
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
        "order": "order",
    }

    def __init__(self, aggregation, *args, **kwargs):
        """
        Options for sorting group by results.

        :param aggregation: Aggregation methods for event platform queries.
        :type aggregation: FormulaAndFunctionEventAggregation

        :param metric: Metric used for sorting group by results.
        :type metric: str, optional

        :param order: Direction of sort.
        :type order: QuerySortOrder, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation

    @classmethod
    def _from_openapi_data(cls, aggregation, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FormulaAndFunctionEventQueryGroupBySort, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation
        return self
