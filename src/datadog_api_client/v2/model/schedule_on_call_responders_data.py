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
    from datadog_api_client.v2.model.schedule_on_call_responders_data_attributes import (
        ScheduleOnCallRespondersDataAttributes,
    )
    from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships import (
        ScheduleOnCallRespondersDataRelationships,
    )
    from datadog_api_client.v2.model.schedule_on_call_responders_data_type import ScheduleOnCallRespondersDataType


class ScheduleOnCallRespondersData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responders_data_attributes import (
            ScheduleOnCallRespondersDataAttributes,
        )
        from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships import (
            ScheduleOnCallRespondersDataRelationships,
        )
        from datadog_api_client.v2.model.schedule_on_call_responders_data_type import ScheduleOnCallRespondersDataType

        return {
            "attributes": (ScheduleOnCallRespondersDataAttributes,),
            "id": (str,),
            "relationships": (ScheduleOnCallRespondersDataRelationships,),
            "type": (ScheduleOnCallRespondersDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: ScheduleOnCallRespondersDataType,
        attributes: Union[ScheduleOnCallRespondersDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[ScheduleOnCallRespondersDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The main data object representing a schedule's on-call responders lookup, including relationships and metadata.

        :param attributes: Attributes for a schedule's on-call responders lookup.
        :type attributes: ScheduleOnCallRespondersDataAttributes, optional

        :param id: Unique identifier of this on-call responders lookup.
        :type id: str, optional

        :param relationships: Relationships for a schedule's on-call responders lookup, including the schedule and its responder groups.
        :type relationships: ScheduleOnCallRespondersDataRelationships, optional

        :param type: Represents the resource type for a schedule's grouped on-call responders across the previous, current, and next positions.
        :type type: ScheduleOnCallRespondersDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
