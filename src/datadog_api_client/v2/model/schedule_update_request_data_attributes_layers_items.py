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
    from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_interval import (
        ScheduleUpdateRequestDataAttributesLayersItemsInterval,
    )
    from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_members_items import (
        ScheduleUpdateRequestDataAttributesLayersItemsMembersItems,
    )
    from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items import (
        ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems,
    )


class ScheduleUpdateRequestDataAttributesLayersItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_interval import (
            ScheduleUpdateRequestDataAttributesLayersItemsInterval,
        )
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_members_items import (
            ScheduleUpdateRequestDataAttributesLayersItemsMembersItems,
        )
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items import (
            ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems,
        )

        return {
            "effective_date": (datetime,),
            "end_date": (datetime,),
            "id": (str,),
            "interval": (ScheduleUpdateRequestDataAttributesLayersItemsInterval,),
            "members": ([ScheduleUpdateRequestDataAttributesLayersItemsMembersItems],),
            "name": (str,),
            "restrictions": ([ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems],),
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
        effective_date: Union[datetime, UnsetType] = unset,
        end_date: Union[datetime, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        interval: Union[ScheduleUpdateRequestDataAttributesLayersItemsInterval, UnsetType] = unset,
        members: Union[List[ScheduleUpdateRequestDataAttributesLayersItemsMembersItems], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        restrictions: Union[List[ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems], UnsetType] = unset,
        rotation_start: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a layer within a schedule update, including rotation details, members,
        and optional restrictions.

        :param effective_date: When this updated layer takes effect (ISO 8601 format).
        :type effective_date: datetime, optional

        :param end_date: When this updated layer should stop being active (ISO 8601 format).
        :type end_date: datetime, optional

        :param id: A unique identifier for the layer being updated.
        :type id: str, optional

        :param interval: Specifies how the rotation repeats: number of days, plus optional seconds, up to the given maximums.
        :type interval: ScheduleUpdateRequestDataAttributesLayersItemsInterval, optional

        :param members: The members assigned to this layer.
        :type members: [ScheduleUpdateRequestDataAttributesLayersItemsMembersItems], optional

        :param name: The name for this layer (for example, “Secondary Coverage”).
        :type name: str, optional

        :param restrictions: Any time restrictions that define when this layer is active.
        :type restrictions: [ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems], optional

        :param rotation_start: The date/time at which the rotation begins (ISO 8601 format).
        :type rotation_start: datetime, optional
        """
        if effective_date is not unset:
            kwargs["effective_date"] = effective_date
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if id is not unset:
            kwargs["id"] = id
        if interval is not unset:
            kwargs["interval"] = interval
        if members is not unset:
            kwargs["members"] = members
        if name is not unset:
            kwargs["name"] = name
        if restrictions is not unset:
            kwargs["restrictions"] = restrictions
        if rotation_start is not unset:
            kwargs["rotation_start"] = rotation_start
        super().__init__(kwargs)
