# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetFieldSort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_sort import WidgetSort

        return {
            "column": (str,),
            "order": (WidgetSort,),
        }

    attribute_map = {
        "column": "column",
        "order": "order",
    }

    def __init__(self, column, order, *args, **kwargs):
        """
        Which column and order to sort by

        :param column: Facet path for the column
        :type column: str

        :param order: Widget sorting methods.
        :type order: WidgetSort
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.column = column
        self.order = order

    @classmethod
    def _from_openapi_data(cls, column, order, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetFieldSort, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.column = column
        self.order = order
        return self
