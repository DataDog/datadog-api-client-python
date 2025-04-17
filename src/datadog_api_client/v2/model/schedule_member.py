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
    from datadog_api_client.v2.model.schedule_member_relationships import ScheduleMemberRelationships
    from datadog_api_client.v2.model.schedule_member_type import ScheduleMemberType


class ScheduleMember(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_member_relationships import ScheduleMemberRelationships
        from datadog_api_client.v2.model.schedule_member_type import ScheduleMemberType

        return {
            "id": (str,),
            "relationships": (ScheduleMemberRelationships,),
            "type": (ScheduleMemberType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: ScheduleMemberType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[ScheduleMemberRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a single member entry in a schedule, referencing a specific user.

        :param id: The unique identifier for this schedule member.
        :type id: str, optional

        :param relationships: Defines relationships for a schedule member, primarily referencing a single user.
        :type relationships: ScheduleMemberRelationships, optional

        :param type: Schedule Members resource type.
        :type type: ScheduleMemberType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
