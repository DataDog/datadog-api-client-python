# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
    from datadog_api_client.v1_20270101.model.logs_transaction_compute import LogsTransactionCompute
    from datadog_api_client.v1_20270101.model.logs_transaction_stream_query_data_source import (
        LogsTransactionStreamQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.logs_transaction_stream_query20270101_sort import (
        LogsTransactionStreamQuery20270101Sort,
    )
    from datadog_api_client.v1_20270101.model.storage_type import StorageType
    from datadog_api_client.v1_20270101.model.logs_transaction_stream_query_version import (
        LogsTransactionStreamQueryVersion,
    )
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort


class LogsTransactionStreamQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
        from datadog_api_client.v1_20270101.model.logs_transaction_compute import LogsTransactionCompute
        from datadog_api_client.v1_20270101.model.logs_transaction_stream_query_data_source import (
            LogsTransactionStreamQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.logs_transaction_stream_query20270101_sort import (
            LogsTransactionStreamQuery20270101Sort,
        )
        from datadog_api_client.v1_20270101.model.storage_type import StorageType
        from datadog_api_client.v1_20270101.model.logs_transaction_stream_query_version import (
            LogsTransactionStreamQueryVersion,
        )

        return {
            "calculated_fields": ([EventsCalculatedField],),
            "compute": ([LogsTransactionCompute],),
            "cross_org_uuids": ([str],),
            "data_source": (LogsTransactionStreamQueryDataSource,),
            "end_query_string": (str,),
            "group_by": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
            "indexes": ([str],),
            "query_string": (str,),
            "sort": (LogsTransactionStreamQuery20270101Sort,),
            "start_query_string": (str,),
            "storage": (StorageType,),
            "version": (LogsTransactionStreamQueryVersion,),
        }

    attribute_map = {
        "calculated_fields": "calculated_fields",
        "compute": "compute",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "end_query_string": "end_query_string",
        "group_by": "group_by",
        "indexes": "indexes",
        "query_string": "query_string",
        "sort": "sort",
        "start_query_string": "start_query_string",
        "storage": "storage",
        "version": "version",
    }

    def __init__(
        self_,
        data_source: LogsTransactionStreamQueryDataSource,
        query_string: str,
        calculated_fields: Union[List[EventsCalculatedField], UnsetType] = unset,
        compute: Union[List[LogsTransactionCompute], UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        end_query_string: Union[str, UnsetType] = unset,
        group_by: Union[List[Any], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        sort: Union[LogsTransactionStreamQuery20270101Sort, ListStreamSort, List[ListStreamSort], UnsetType] = unset,
        start_query_string: Union[str, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        version: Union[LogsTransactionStreamQueryVersion, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param calculated_fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type calculated_fields: [EventsCalculatedField], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [LogsTransactionCompute], optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: LogsTransactionStreamQueryDataSource

        :param end_query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type end_query_string: str, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [bool, date, datetime, dict, float, int, list, str, UUID, none_type], optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: LogsTransactionStreamQuery20270101Sort, optional

        :param start_query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type start_query_string: str, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param version: Test-only generated schema for the dashboard versioning proof of concept.
        :type version: LogsTransactionStreamQueryVersion, optional
        """
        if calculated_fields is not unset:
            kwargs["calculated_fields"] = calculated_fields
        if compute is not unset:
            kwargs["compute"] = compute
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if end_query_string is not unset:
            kwargs["end_query_string"] = end_query_string
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if sort is not unset:
            kwargs["sort"] = sort
        if start_query_string is not unset:
            kwargs["start_query_string"] = start_query_string
        if storage is not unset:
            kwargs["storage"] = storage
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
