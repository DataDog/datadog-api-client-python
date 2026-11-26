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
    from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
    from datadog_api_client.v1_20270101.model.logs_query_compute import LogsQueryCompute
    from datadog_api_client.v1_20270101.model.log_query_definition_group_by import LogQueryDefinitionGroupBy
    from datadog_api_client.v1_20270101.model.log_query_definition_search import LogQueryDefinitionSearch
    from datadog_api_client.v1_20270101.model.storage_type import StorageType


class LogQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
        from datadog_api_client.v1_20270101.model.logs_query_compute import LogsQueryCompute
        from datadog_api_client.v1_20270101.model.log_query_definition_group_by import LogQueryDefinitionGroupBy
        from datadog_api_client.v1_20270101.model.log_query_definition_search import LogQueryDefinitionSearch
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "calculated_fields": ([EventsCalculatedField],),
            "compute": (LogsQueryCompute,),
            "group_by": ([LogQueryDefinitionGroupBy],),
            "index": (str,),
            "multi_compute": ([LogsQueryCompute],),
            "search": (LogQueryDefinitionSearch,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "calculated_fields": "calculated_fields",
        "compute": "compute",
        "group_by": "group_by",
        "index": "index",
        "multi_compute": "multi_compute",
        "search": "search",
        "storage": "storage",
    }

    def __init__(
        self_,
        calculated_fields: Union[List[EventsCalculatedField], UnsetType] = unset,
        compute: Union[LogsQueryCompute, UnsetType] = unset,
        group_by: Union[List[LogQueryDefinitionGroupBy], UnsetType] = unset,
        index: Union[str, UnsetType] = unset,
        multi_compute: Union[List[LogsQueryCompute], UnsetType] = unset,
        search: Union[LogQueryDefinitionSearch, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param calculated_fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type calculated_fields: [EventsCalculatedField], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: LogsQueryCompute, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [LogQueryDefinitionGroupBy], optional

        :param index: Test-only generated schema for the dashboard versioning proof of concept.
        :type index: str, optional

        :param multi_compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type multi_compute: [LogsQueryCompute], optional

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: LogQueryDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if calculated_fields is not unset:
            kwargs["calculated_fields"] = calculated_fields
        if compute is not unset:
            kwargs["compute"] = compute
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if index is not unset:
            kwargs["index"] = index
        if multi_compute is not unset:
            kwargs["multi_compute"] = multi_compute
        if search is not unset:
            kwargs["search"] = search
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)
