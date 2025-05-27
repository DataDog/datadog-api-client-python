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
    from datadog_api_client.v2.model.schedule_update_request_data_attributes import ScheduleUpdateRequestDataAttributes
    from datadog_api_client.v2.model.schedule_update_request_data_relationships import (
        ScheduleUpdateRequestDataRelationships,
    )
    from datadog_api_client.v2.model.schedule_update_request_data_type import ScheduleUpdateRequestDataType


class ScheduleUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data_attributes import (
            ScheduleUpdateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.schedule_update_request_data_relationships import (
            ScheduleUpdateRequestDataRelationships,
        )
        from datadog_api_client.v2.model.schedule_update_request_data_type import ScheduleUpdateRequestDataType

        return {
            "attributes": (ScheduleUpdateRequestDataAttributes,),
            "id": (str,),
            "relationships": (ScheduleUpdateRequestDataRelationships,),
            "type": (ScheduleUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ScheduleUpdateRequestDataAttributes,
        id: str,
        type: ScheduleUpdateRequestDataType,
        relationships: Union[ScheduleUpdateRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Contains all data needed to update an existing schedule, including its attributes (such as name and time zone) and any relationships to teams.

        :param attributes: Defines the updatable attributes for a schedule, such as name, time zone, and layers.
        :type attributes: ScheduleUpdateRequestDataAttributes

        :param id: The ID of the schedule to be updated.
        :type id: str

        :param relationships: Houses relationships for the schedule update, typically referencing teams.
        :type relationships: ScheduleUpdateRequestDataRelationships, optional

        :param type: Schedules resource type.
        :type type: ScheduleUpdateRequestDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
