# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogQueryDefinitionGroupBySort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_sort import WidgetSort

        return {
            "aggregation": (str,),
            "facet": (str,),
            "order": (WidgetSort,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "facet": "facet",
        "order": "order",
    }

    def __init__(self, aggregation, order, *args, **kwargs):
        """
        Define a sorting method.

        :param aggregation: The aggregation method.
        :type aggregation: str

        :param facet: Facet name.
        :type facet: str, optional

        :param order: Widget sorting methods.
        :type order: WidgetSort
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation
        self.order = order

    @classmethod
    def _from_openapi_data(cls, aggregation, order, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogQueryDefinitionGroupBySort, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation
        self.order = order
        return self
