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
    from datadog_api_client.v1_20270101.model.composite_events_platform_query_search import (
        CompositeEventsPlatformQuerySearch,
    )
    from datadog_api_client.v1_20270101.model.storage_type import StorageType


class CompositeEventsPlatformQuery(ModelNormal):
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
        from datadog_api_client.v1_20270101.model.composite_events_platform_query_search import (
            CompositeEventsPlatformQuerySearch,
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
            "search": (CompositeEventsPlatformQuerySearch,),
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
        data_source: FormulaAndFunctionEventsDataSource,
        name: str,
        columns: Union[List[ListColumn], UnsetType] = unset,
        compute: Union[List[AggregateCompute], UnsetType] = unset,
        compute_count: Union[bool, UnsetType] = unset,
        group_by: Union[List[FormulaAndFunctionEventQueryGroupBy], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        search: Union[CompositeEventsPlatformQuerySearch, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [ListColumn], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [AggregateCompute], optional

        :param compute_count: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute_count: bool, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaAndFunctionEventsDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [FormulaAndFunctionEventQueryGroupBy], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: CompositeEventsPlatformQuerySearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if compute is not unset:
            kwargs["compute"] = compute
        if compute_count is not unset:
            kwargs["compute_count"] = compute_count
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if search is not unset:
            kwargs["search"] = search
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
