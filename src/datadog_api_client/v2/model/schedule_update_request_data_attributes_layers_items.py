# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.layer_attributes_interval import LayerAttributesInterval
    from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items import (
        ScheduleRequestDataAttributesLayersItemsMembersItems,
    )
    from datadog_api_client.v2.model.time_restriction import TimeRestriction


class ScheduleUpdateRequestDataAttributesLayersItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.layer_attributes_interval import LayerAttributesInterval
        from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items import (
            ScheduleRequestDataAttributesLayersItemsMembersItems,
        )
        from datadog_api_client.v2.model.time_restriction import TimeRestriction

        return {
            "effective_date": (datetime,),
            "end_date": (datetime,),
            "id": (str,),
            "interval": (LayerAttributesInterval,),
            "members": ([ScheduleRequestDataAttributesLayersItemsMembersItems],),
            "name": (str,),
            "restrictions": ([TimeRestriction],),
            "rotation_start": (datetime,),
        }

    attribute_map = {
        "effective_date": "effective_date",
        "end_date": "end_date",
        "id": "id",
        "interval": "interval",
        "members": "members",
        "name": "name",
        "restrictions": "restrictions",
        "rotation_start": "rotation_start",
    }

    def __init__(
        self_,
        effective_date: datetime,
        interval: LayerAttributesInterval,
        members: List[ScheduleRequestDataAttributesLayersItemsMembersItems],
        name: str,
        rotation_start: datetime,
        end_date: Union[datetime, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        restrictions: Union[List[TimeRestriction], UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a layer within a schedule update, including rotation details, members,
        and optional restrictions.

        :param effective_date: When this updated layer takes effect (ISO 8601 format).
        :type effective_date: datetime

        :param end_date: When this updated layer should stop being active (ISO 8601 format).
        :type end_date: datetime, optional

        :param id: A unique identifier for the layer being updated.
        :type id: str, optional

        :param interval: Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
        :type interval: LayerAttributesInterval

        :param members: The members assigned to this layer.
        :type members: [ScheduleRequestDataAttributesLayersItemsMembersItems]

        :param name: The name for this layer (for example, "Secondary Coverage").
        :type name: str

        :param restrictions: Any time restrictions that define when this layer is active.
        :type restrictions: [TimeRestriction], optional

        :param rotation_start: The date/time at which the rotation begins (ISO 8601 format).
        :type rotation_start: datetime
        """
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if id is not unset:
            kwargs["id"] = id
        if restrictions is not unset:
            kwargs["restrictions"] = restrictions
        super().__init__(kwargs)

        self_.effective_date = effective_date
        self_.interval = interval
        self_.members = members
        self_.name = name
        self_.rotation_start = rotation_start
