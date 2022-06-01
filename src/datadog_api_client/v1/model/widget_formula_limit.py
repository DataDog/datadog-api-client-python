# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetFormulaLimit(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.query_sort_order import QuerySortOrder

        return {
            "count": (int,),
            "order": (QuerySortOrder,),
        }

    attribute_map = {
        "count": "count",
        "order": "order",
    }

    def __init__(self, *args, **kwargs):
        """
        Options for limiting results returned.

        :param count: Number of results to return.
        :type count: int, optional

        :param order: Direction of sort.
        :type order: QuerySortOrder, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetFormulaLimit, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
