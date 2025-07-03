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


class ScheduleCreateRequestDataAttributesLayersItems(ModelNormal):
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
            "interval": (LayerAttributesInterval,),
            "members": ([ScheduleRequestDataAttributesLayersItemsMembersItems],),
            "name": (str,),
            "restrictions": ([TimeRestriction],),
            "rotation_start": (datetime,),
        }

    attribute_map = {
        "effective_date": "effective_date",
        "end_date": "end_date",
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
        restrictions: Union[List[TimeRestriction], UnsetType] = unset,
        **kwargs,
    ):
        """
        Describes a schedule layer, including rotation intervals, members, restrictions, and timeline settings.

        :param effective_date: The date/time when this layer becomes active (in ISO 8601).
        :type effective_date: datetime

        :param end_date: The date/time after which this layer no longer applies (in ISO 8601).
        :type end_date: datetime, optional

        :param interval: Defines how often the rotation repeats, using a combination of days and optional seconds. Should be at least 1 hour.
        :type interval: LayerAttributesInterval

        :param members: A list of members who participate in this layer's rotation.
        :type members: [ScheduleRequestDataAttributesLayersItemsMembersItems]

        :param name: The name of this layer.
        :type name: str

        :param restrictions: Zero or more time-based restrictions (for example, only weekdays, during business hours).
        :type restrictions: [TimeRestriction], optional

        :param rotation_start: The date/time when the rotation for this layer starts (in ISO 8601).
        :type rotation_start: datetime
        """
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if restrictions is not unset:
            kwargs["restrictions"] = restrictions
        super().__init__(kwargs)

        self_.effective_date = effective_date
        self_.interval = interval
        self_.members = members
        self_.name = name
        self_.rotation_start = rotation_start
