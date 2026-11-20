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
    from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
    from datadog_api_client.v1_20270101.model.advanced_event_platform_source import AdvancedEventPlatformSource
    from datadog_api_client.v1_20270101.model.event_platform_dataset_definition_search import (
        EventPlatformDatasetDefinitionSearch,
    )
    from datadog_api_client.v1_20270101.model.storage_type import StorageType
    from datadog_api_client.v1_20270101.model.time_window import TimeWindow


class EventPlatformDatasetDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
        from datadog_api_client.v1_20270101.model.advanced_event_platform_source import AdvancedEventPlatformSource
        from datadog_api_client.v1_20270101.model.event_platform_dataset_definition_search import (
            EventPlatformDatasetDefinitionSearch,
        )
        from datadog_api_client.v1_20270101.model.storage_type import StorageType
        from datadog_api_client.v1_20270101.model.time_window import TimeWindow

        return {
            "columns": ([DatasetColumn],),
            "data_source": (AdvancedEventPlatformSource,),
            "indexes": ([str],),
            "name": (str,),
            "search": (EventPlatformDatasetDefinitionSearch,),
            "storage": (StorageType,),
            "time_window": (TimeWindow,),
        }

    attribute_map = {
        "columns": "columns",
        "data_source": "data_source",
        "indexes": "indexes",
        "name": "name",
        "search": "search",
        "storage": "storage",
        "time_window": "time_window",
    }

    def __init__(
        self_,
        columns: List[DatasetColumn],
        data_source: AdvancedEventPlatformSource,
        name: str,
        indexes: Union[List[str], UnsetType] = unset,
        search: Union[EventPlatformDatasetDefinitionSearch, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        time_window: Union[TimeWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [DatasetColumn]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: AdvancedEventPlatformSource

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: EventPlatformDatasetDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param time_window: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_window: TimeWindow, optional
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if search is not unset:
            kwargs["search"] = search
        if storage is not unset:
            kwargs["storage"] = storage
        if time_window is not unset:
            kwargs["time_window"] = time_window
        super().__init__(kwargs)

        self_.columns = columns
        self_.data_source = data_source
        self_.name = name
