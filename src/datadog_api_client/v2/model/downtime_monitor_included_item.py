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
    from datadog_api_client.v2.model.downtime_monitor_included_attributes import DowntimeMonitorIncludedAttributes
    from datadog_api_client.v2.model.downtime_included_monitor_type import DowntimeIncludedMonitorType


class DowntimeMonitorIncludedItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_monitor_included_attributes import DowntimeMonitorIncludedAttributes
        from datadog_api_client.v2.model.downtime_included_monitor_type import DowntimeIncludedMonitorType

        return {
            "attributes": (DowntimeMonitorIncludedAttributes,),
            "id": (int,),
            "type": (DowntimeIncludedMonitorType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DowntimeMonitorIncludedAttributes, UnsetType] = unset,
        id: Union[int, UnsetType] = unset,
        type: Union[DowntimeIncludedMonitorType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about the monitor identified by the downtime.

        :param attributes: Attributes of the monitor identified by the downtime.
        :type attributes: DowntimeMonitorIncludedAttributes, optional

        :param id: ID of the monitor identified by the downtime.
        :type id: int, optional

        :param type: Monitor resource type.
        :type type: DowntimeIncludedMonitorType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
