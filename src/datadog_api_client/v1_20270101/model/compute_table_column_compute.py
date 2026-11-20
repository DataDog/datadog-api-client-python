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
    from datadog_api_client.v1_20270101.model.table_column_modifier import TableColumnModifier
    from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator


class ComputeTableColumnCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_column_modifier import TableColumnModifier
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator

        return {
            "aggregation": (str,),
            "filter": (str,),
            "modifiers": ([TableColumnModifier],),
            "_property": (str,),
            "query": (str,),
            "scalar_aggregation": (ScalarAggregator,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "filter": "filter",
        "modifiers": "modifiers",
        "_property": "property",
        "query": "query",
        "scalar_aggregation": "scalar_aggregation",
    }

    def __init__(
        self_,
        aggregation: str,
        query: str,
        filter: Union[str, UnsetType] = unset,
        modifiers: Union[List[TableColumnModifier], UnsetType] = unset,
        _property: Union[str, UnsetType] = unset,
        scalar_aggregation: Union[ScalarAggregator, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: str

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param modifiers: Test-only generated schema for the dashboard versioning proof of concept.
        :type modifiers: [TableColumnModifier], optional

        :param _property: Test-only generated schema for the dashboard versioning proof of concept.
        :type _property: str, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str

        :param scalar_aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type scalar_aggregation: ScalarAggregator, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if modifiers is not unset:
            kwargs["modifiers"] = modifiers
        if _property is not unset:
            kwargs["_property"] = _property
        if scalar_aggregation is not unset:
            kwargs["scalar_aggregation"] = scalar_aggregation
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.query = query
