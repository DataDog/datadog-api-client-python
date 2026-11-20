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
    from datadog_api_client.v1_20270101.model.event_pattern_stream_query_data_source import (
        EventPatternStreamQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.event_pattern_group_by import EventPatternGroupBy
    from datadog_api_client.v1_20270101.model.event_pattern_stream_query20270101_sort import (
        EventPatternStreamQuery20270101Sort,
    )
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort


class EventPatternStreamQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
        from datadog_api_client.v1_20270101.model.event_pattern_stream_query_data_source import (
            EventPatternStreamQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.event_pattern_group_by import EventPatternGroupBy
        from datadog_api_client.v1_20270101.model.event_pattern_stream_query20270101_sort import (
            EventPatternStreamQuery20270101Sort,
        )

        return {
            "calculated_fields": ([EventsCalculatedField],),
            "clustering_pattern_field_path": (str,),
            "cross_org_uuids": ([str],),
            "data_source": (EventPatternStreamQueryDataSource,),
            "group_by": ([EventPatternGroupBy],),
            "indexes": ([str],),
            "query_string": (str,),
            "sort": (EventPatternStreamQuery20270101Sort,),
        }

    attribute_map = {
        "calculated_fields": "calculated_fields",
        "clustering_pattern_field_path": "clustering_pattern_field_path",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "group_by": "group_by",
        "indexes": "indexes",
        "query_string": "query_string",
        "sort": "sort",
    }

    def __init__(
        self_,
        data_source: EventPatternStreamQueryDataSource,
        query_string: str,
        calculated_fields: Union[List[EventsCalculatedField], UnsetType] = unset,
        clustering_pattern_field_path: Union[str, UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        group_by: Union[List[EventPatternGroupBy], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        sort: Union[EventPatternStreamQuery20270101Sort, ListStreamSort, List[ListStreamSort], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param calculated_fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type calculated_fields: [EventsCalculatedField], optional

        :param clustering_pattern_field_path: Test-only generated schema for the dashboard versioning proof of concept.
        :type clustering_pattern_field_path: str, optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: EventPatternStreamQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [EventPatternGroupBy], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: EventPatternStreamQuery20270101Sort, optional
        """
        if calculated_fields is not unset:
            kwargs["calculated_fields"] = calculated_fields
        if clustering_pattern_field_path is not unset:
            kwargs["clustering_pattern_field_path"] = clustering_pattern_field_path
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
