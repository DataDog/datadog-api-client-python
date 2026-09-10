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
    from datadog_api_client.v2.model.schedule_data_attributes import ScheduleDataAttributes
    from datadog_api_client.v2.model.schedule_list_item_relationships import ScheduleListItemRelationships
    from datadog_api_client.v2.model.schedule_data_type import ScheduleDataType


class ScheduleListItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_data_attributes import ScheduleDataAttributes
        from datadog_api_client.v2.model.schedule_list_item_relationships import ScheduleListItemRelationships
        from datadog_api_client.v2.model.schedule_data_type import ScheduleDataType

        return {
            "attributes": (ScheduleDataAttributes,),
            "id": (str,),
            "relationships": (ScheduleListItemRelationships,),
            "type": (ScheduleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ScheduleDataType,
        attributes: Union[ScheduleDataAttributes, UnsetType] = unset,
        relationships: Union[ScheduleListItemRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a summary of a schedule, linking its core attributes and team relationships.

        :param attributes: Provides core properties of a schedule object such as its name and time zone.
        :type attributes: ScheduleDataAttributes, optional

        :param id: The schedule's unique identifier.
        :type id: str

        :param relationships: Groups the relationships for a schedule summary, referencing its teams.
        :type relationships: ScheduleListItemRelationships, optional

        :param type: Schedules resource type.
        :type type: ScheduleDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
