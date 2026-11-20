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
    from datadog_api_client.v1_20270101.model.events_query_fragment_definition_data_source import (
        EventsQueryFragmentDefinitionDataSource,
    )
    from datadog_api_client.v1_20270101.model.events_query_fragment_definition_search import (
        EventsQueryFragmentDefinitionSearch,
    )
    from datadog_api_client.v1_20270101.model.storage_type import StorageType


class EventsQueryFragmentDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_query_fragment_definition_data_source import (
            EventsQueryFragmentDefinitionDataSource,
        )
        from datadog_api_client.v1_20270101.model.events_query_fragment_definition_search import (
            EventsQueryFragmentDefinitionSearch,
        )
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "alias": (str,),
            "data_source": (EventsQueryFragmentDefinitionDataSource,),
            "indexes": ([str],),
            "name": (str,),
            "search": (EventsQueryFragmentDefinitionSearch,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "alias": "alias",
        "data_source": "data_source",
        "indexes": "indexes",
        "name": "name",
        "search": "search",
        "storage": "storage",
    }

    def __init__(
        self_,
        data_source: EventsQueryFragmentDefinitionDataSource,
        name: str,
        alias: Union[str, UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        search: Union[EventsQueryFragmentDefinitionSearch, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: EventsQueryFragmentDefinitionDataSource

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: EventsQueryFragmentDefinitionSearch, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if search is not unset:
            kwargs["search"] = search
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
