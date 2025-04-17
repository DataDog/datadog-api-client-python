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
    from datadog_api_client.v2.model.schedule_user_attributes import ScheduleUserAttributes
    from datadog_api_client.v2.model.schedule_user_type import ScheduleUserType


class ScheduleUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_user_attributes import ScheduleUserAttributes
        from datadog_api_client.v2.model.schedule_user_type import ScheduleUserType

        return {
            "attributes": (ScheduleUserAttributes,),
            "id": (str,),
            "type": (ScheduleUserType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ScheduleUserType,
        attributes: Union[ScheduleUserAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents a user object in the context of a schedule, including their ``id`` , type, and basic attributes.

        :param attributes: Provides basic user information for a schedule, including a name and email address.
        :type attributes: ScheduleUserAttributes, optional

        :param id: The unique user identifier.
        :type id: str, optional

        :param type: Users resource type.
        :type type: ScheduleUserType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
