# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FlatSortBy20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (HeatGridSortAggregation,),
            "order": (QuerySortOrder,),
            "_property": (FlatSortByAnyOfAnyOfItemProperty,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "order": "order",
        "_property": "property",
    }

    def __init__(
        self_,
        aggregation: HeatGridSortAggregation,
        order: QuerySortOrder,
        _property: FlatSortByAnyOfAnyOfItemProperty,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: HeatGridSortAggregation

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder

        :param _property: Test-only generated schema for the dashboard versioning proof of concept.
        :type _property: FlatSortByAnyOfAnyOfItemProperty
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.order = order
        self_._property = _property
