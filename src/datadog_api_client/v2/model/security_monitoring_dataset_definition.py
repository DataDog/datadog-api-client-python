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
    from datadog_api_client.v2.model.security_monitoring_dataset_column import SecurityMonitoringDatasetColumn
    from datadog_api_client.v2.model.security_monitoring_dataset_search import SecurityMonitoringDatasetSearch
    from datadog_api_client.v2.model.security_monitoring_dataset_time_window import SecurityMonitoringDatasetTimeWindow


class SecurityMonitoringDatasetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_column import SecurityMonitoringDatasetColumn
        from datadog_api_client.v2.model.security_monitoring_dataset_search import SecurityMonitoringDatasetSearch
        from datadog_api_client.v2.model.security_monitoring_dataset_time_window import (
            SecurityMonitoringDatasetTimeWindow,
        )

        return {
            "columns": ([SecurityMonitoringDatasetColumn],),
            "data_source": (str,),
            "indexes": ([str],),
            "name": (str,),
            "query_filter": (str,),
            "search": (SecurityMonitoringDatasetSearch,),
            "storage": (str,),
            "table_name": (str,),
            "time_window": (SecurityMonitoringDatasetTimeWindow,),
        }

    attribute_map = {
        "columns": "columns",
        "data_source": "data_source",
        "indexes": "indexes",
        "name": "name",
        "query_filter": "query_filter",
        "search": "search",
        "storage": "storage",
        "table_name": "table_name",
        "time_window": "time_window",
    }

    def __init__(
        self_,
        data_source: str,
        name: str,
        columns: Union[List[SecurityMonitoringDatasetColumn], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        search: Union[SecurityMonitoringDatasetSearch, UnsetType] = unset,
        storage: Union[str, UnsetType] = unset,
        table_name: Union[str, UnsetType] = unset,
        time_window: Union[SecurityMonitoringDatasetTimeWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the dataset. The shape depends on the value of ``data_source``.
        Use ``reference_table`` or ``managed_resource`` for a referential dataset, or one of the
        event platform sources (for example ``logs`` , ``audit`` , ``events`` , ``spans`` , ``rum`` ) for
        an event platform dataset.

        :param columns: For event platform datasets, the list of columns exposed by the dataset.
        :type columns: [SecurityMonitoringDatasetColumn], optional

        :param data_source: The data source backing this dataset definition.
        :type data_source: str

        :param indexes: For event platform datasets, the list of indexes to query.
        :type indexes: [str], optional

        :param name: The unique name of the dataset. Must start with a lowercase letter and contain only lowercase letters, digits, and underscores (max 255 characters).
        :type name: str

        :param query_filter: For referential datasets, an optional filter expression applied to the table.
        :type query_filter: str, optional

        :param search: The search clause applied to an event platform dataset.
        :type search: SecurityMonitoringDatasetSearch, optional

        :param storage: Storage tier the dataset reads from. Applies to event platform datasets.
        :type storage: str, optional

        :param table_name: For referential datasets, the name of the underlying table.
        :type table_name: str, optional

        :param time_window: An optional time window that overrides the default query time range.
        :type time_window: SecurityMonitoringDatasetTimeWindow, optional
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if search is not unset:
            kwargs["search"] = search
        if storage is not unset:
            kwargs["storage"] = storage
        if table_name is not unset:
            kwargs["table_name"] = table_name
        if time_window is not unset:
            kwargs["time_window"] = time_window
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
