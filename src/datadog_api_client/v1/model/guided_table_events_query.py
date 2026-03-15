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
    from datadog_api_client.v1.model.guided_table_events_query_data_source import GuidedTableEventsQueryDataSource
    from datadog_api_client.v1.model.guided_table_events_query_search import GuidedTableEventsQuerySearch
    from datadog_api_client.v1.model.guided_table_storage_type import GuidedTableStorageType


class GuidedTableEventsQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_events_query_data_source import GuidedTableEventsQueryDataSource
        from datadog_api_client.v1.model.guided_table_events_query_search import GuidedTableEventsQuerySearch
        from datadog_api_client.v1.model.guided_table_storage_type import GuidedTableStorageType

        return {
            "alias": (str,),
            "data_source": (GuidedTableEventsQueryDataSource,),
            "indexes": ([str],),
            "name": (str,),
            "search": (GuidedTableEventsQuerySearch,),
            "storage": (GuidedTableStorageType,),
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
        data_source: GuidedTableEventsQueryDataSource,
        name: str,
        alias: Union[str, UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        search: Union[GuidedTableEventsQuerySearch, UnsetType] = unset,
        storage: Union[GuidedTableStorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        An events-platform query fragment used as source data for a guided table. Covers logs, RUM, spans, CI pipelines, events, and product analytics.

        :param alias: Display alias for the query.
        :type alias: str, optional

        :param data_source: Events data source.
        :type data_source: GuidedTableEventsQueryDataSource

        :param indexes: Indexes to search for events.
        :type indexes: [str], optional

        :param name: Variable name used to reference this query in columns and formulas.
        :type name: str

        :param search: Search filter for matching events.
        :type search: GuidedTableEventsQuerySearch, optional

        :param storage: Storage tier to target for an events-platform query in a guided table.
        :type storage: GuidedTableStorageType, optional
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
