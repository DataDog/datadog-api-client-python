# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.data_observability_monitor_group_by_values import (
        DataObservabilityMonitorGroupByValues,
    )
    from datadog_api_client.v2.model.data_observability_monitor_group_status import DataObservabilityMonitorGroupStatus


class DataObservabilityMonitorRunGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_observability_monitor_group_by_values import (
            DataObservabilityMonitorGroupByValues,
        )
        from datadog_api_client.v2.model.data_observability_monitor_group_status import (
            DataObservabilityMonitorGroupStatus,
        )

        return {
            "account": (str,),
            "column": (str,),
            "database": (str,),
            "entity_id": (str,),
            "entity_type": (str,),
            "group": (str,),
            "group_by_values": (DataObservabilityMonitorGroupByValues,),
            "platform": (str,),
            "schema": (str,),
            "status": (DataObservabilityMonitorGroupStatus,),
            "table": (str,),
        }

    attribute_map = {
        "account": "account",
        "column": "column",
        "database": "database",
        "entity_id": "entity_id",
        "entity_type": "entity_type",
        "group": "group",
        "group_by_values": "group_by_values",
        "platform": "platform",
        "schema": "schema",
        "status": "status",
        "table": "table",
    }

    def __init__(
        self_,
        database: str,
        entity_id: str,
        entity_type: str,
        group: str,
        platform: str,
        status: DataObservabilityMonitorGroupStatus,
        account: Union[str, UnsetType] = unset,
        column: Union[str, UnsetType] = unset,
        group_by_values: Union[DataObservabilityMonitorGroupByValues, UnsetType] = unset,
        schema: Union[str, UnsetType] = unset,
        table: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A monitor group that is not ok after a run.

        :param account: The account of the entity, when the platform has one.
        :type account: str, optional

        :param column: The column of the entity, when it is a column.
        :type column: str, optional

        :param database: The database of the entity.
        :type database: str

        :param entity_id: The ID of the table or column the group checks.
        :type entity_id: str

        :param entity_type: The type of the entity, such as table or column.
        :type entity_type: str

        :param group: The group's name in Datadog monitors, as the monitor API and UI show it. Pass it as ``filter[group]`` to list the group's evaluations.
        :type group: str

        :param group_by_values: The values of the monitor's group-by columns for this group. ``N/A`` means the column had no value.
        :type group_by_values: DataObservabilityMonitorGroupByValues, optional

        :param platform: The data platform of the entity.
        :type platform: str

        :param schema: The schema of the entity, when it has one.
        :type schema: str, optional

        :param status: The state of a monitor group, from the alerting engine.
        :type status: DataObservabilityMonitorGroupStatus

        :param table: The table of the entity, when it is a table or column.
        :type table: str, optional
        """
        if account is not unset:
            kwargs["account"] = account
        if column is not unset:
            kwargs["column"] = column
        if group_by_values is not unset:
            kwargs["group_by_values"] = group_by_values
        if schema is not unset:
            kwargs["schema"] = schema
        if table is not unset:
            kwargs["table"] = table
        super().__init__(kwargs)

        self_.database = database
        self_.entity_id = entity_id
        self_.entity_type = entity_type
        self_.group = group
        self_.platform = platform
        self_.status = status
