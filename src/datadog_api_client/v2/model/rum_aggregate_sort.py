# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMAggregateSort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_aggregation_function import RUMAggregationFunction
        from datadog_api_client.v2.model.rum_sort_order import RUMSortOrder
        from datadog_api_client.v2.model.rum_aggregate_sort_type import RUMAggregateSortType

        return {
            "aggregation": (RUMAggregationFunction,),
            "metric": (str,),
            "order": (RUMSortOrder,),
            "type": (RUMAggregateSortType,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
        "order": "order",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        A sort rule.

        :param aggregation: An aggregation function.
        :type aggregation: RUMAggregationFunction, optional

        :param metric: The metric to sort by (only used for ``type=measure`` ).
        :type metric: str, optional

        :param order: The order to use, ascending or descending.
        :type order: RUMSortOrder, optional

        :param type: The type of sorting algorithm.
        :type type: RUMAggregateSortType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMAggregateSort, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
