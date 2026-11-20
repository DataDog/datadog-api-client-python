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
    from datadog_api_client.v1_20270101.model.events_context import EventsContext
    from datadog_api_client.v1_20270101.model.logs_stream_query_data_source import LogsStreamQueryDataSource
    from datadog_api_client.v1_20270101.model.events_data_extraction import EventsDataExtraction
    from datadog_api_client.v1_20270101.model.logs_stream_query20270101_sort import LogsStreamQuery20270101Sort
    from datadog_api_client.v1_20270101.model.storage_type import StorageType
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort


class LogsStreamQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
        from datadog_api_client.v1_20270101.model.events_context import EventsContext
        from datadog_api_client.v1_20270101.model.logs_stream_query_data_source import LogsStreamQueryDataSource
        from datadog_api_client.v1_20270101.model.events_data_extraction import EventsDataExtraction
        from datadog_api_client.v1_20270101.model.logs_stream_query20270101_sort import LogsStreamQuery20270101Sort
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "calculated_fields": ([EventsCalculatedField],),
            "context": (EventsContext,),
            "cross_org_uuids": ([str],),
            "data_source": (LogsStreamQueryDataSource,),
            "extractions": ([EventsDataExtraction],),
            "indexes": ([str],),
            "query_string": (str,),
            "sort": (LogsStreamQuery20270101Sort,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "calculated_fields": "calculated_fields",
        "context": "context",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "extractions": "extractions",
        "indexes": "indexes",
        "query_string": "query_string",
        "sort": "sort",
        "storage": "storage",
    }

    def __init__(
        self_,
        data_source: LogsStreamQueryDataSource,
        query_string: str,
        calculated_fields: Union[List[EventsCalculatedField], UnsetType] = unset,
        context: Union[EventsContext, UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        extractions: Union[List[EventsDataExtraction], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        sort: Union[LogsStreamQuery20270101Sort, ListStreamSort, List[ListStreamSort], UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param calculated_fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type calculated_fields: [EventsCalculatedField], optional

        :param context: Test-only generated schema for the dashboard versioning proof of concept.
        :type context: EventsContext, optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: LogsStreamQueryDataSource

        :param extractions: Test-only generated schema for the dashboard versioning proof of concept.
        :type extractions: [EventsDataExtraction], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: LogsStreamQuery20270101Sort, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if calculated_fields is not unset:
            kwargs["calculated_fields"] = calculated_fields
        if context is not unset:
            kwargs["context"] = context
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if extractions is not unset:
            kwargs["extractions"] = extractions
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if sort is not unset:
            kwargs["sort"] = sort
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
