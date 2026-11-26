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
    from datadog_api_client.v1_20270101.model.list_column import ListColumn
    from datadog_api_client.v1_20270101.model.aggregate_compute import AggregateCompute
    from datadog_api_client.v1_20270101.model.formula_and_function_events_data_source import (
        FormulaAndFunctionEventsDataSource,
    )
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by import (
        FormulaAndFunctionEventQueryGroupBy,
    )
    from datadog_api_client.v1_20270101.model.composite_events_platform_sub_query_definition_search import (
        CompositeEventsPlatformSubQueryDefinitionSearch,
    )
    from datadog_api_client.v1_20270101.model.storage_type import StorageType


class CompositeEventsPlatformSubQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.list_column import ListColumn
        from datadog_api_client.v1_20270101.model.aggregate_compute import AggregateCompute
        from datadog_api_client.v1_20270101.model.formula_and_function_events_data_source import (
            FormulaAndFunctionEventsDataSource,
        )
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by import (
            FormulaAndFunctionEventQueryGroupBy,
        )
        from datadog_api_client.v1_20270101.model.composite_events_platform_sub_query_definition_search import (
            CompositeEventsPlatformSubQueryDefinitionSearch,
        )
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "columns": ([ListColumn],),
            "compute": ([AggregateCompute],),
            "compute_count": (bool,),
            "data_source": (FormulaAndFunctionEventsDataSource,),
            "group_by": ([FormulaAndFunctionEventQueryGroupBy],),
            "indexes": ([str],),
            "name": (str,),
            "search": (CompositeEventsPlatformSubQueryDefinitionSearch,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "columns": "columns",
        "compute": "compute",
        "compute_count": "compute_count",
        "data_source": "data_source",
        "group_by": "group_by",
        "indexes": "indexes",
        "name": "name",
        "search": "search",
        "storage": "storage",
    }

    def __init__(
        self_,
        compute: List[AggregateCompute],
        data_source: FormulaAndFunctionEventsDataSource,
        group_by: List[FormulaAndFunctionEventQueryGroupBy],
        name: str,
        columns: Union[List[ListColumn], UnsetType] = unset,
        compute_count: Union[bool, UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        search: Union[CompositeEventsPlatformSubQueryDefinitionSearch, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [ListColumn], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [AggregateCompute]

        :param compute_count: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute_count: bool, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaAndFunctionEventsDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [FormulaAndFunctionEventQueryGroupBy]

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: CompositeEventsPlatformSubQueryDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if compute_count is not unset:
            kwargs["compute_count"] = compute_count
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if search is not unset:
            kwargs["search"] = search
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.group_by = group_by
        self_.name = name
