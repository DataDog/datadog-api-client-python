# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.downtime_relationships_monitor_data import DowntimeRelationshipsMonitorData


class DowntimeRelationshipsMonitor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_relationships_monitor_data import DowntimeRelationshipsMonitorData

        return {
            "data": (DowntimeRelationshipsMonitorData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[DowntimeRelationshipsMonitorData, none_type, UnsetType] = unset, **kwargs):
        """
        The monitor identified by the downtime.

        :param data: Data for the monitor.
        :type data: DowntimeRelationshipsMonitorData, none_type, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
