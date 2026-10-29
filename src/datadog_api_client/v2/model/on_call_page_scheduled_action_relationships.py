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
    from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships_schedules import (
        OnCallPageScheduledActionRelationshipsSchedules,
    )
    from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships_users import (
        OnCallPageScheduledActionRelationshipsUsers,
    )


class OnCallPageScheduledActionRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships_schedules import (
            OnCallPageScheduledActionRelationshipsSchedules,
        )
        from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships_users import (
            OnCallPageScheduledActionRelationshipsUsers,
        )

        return {
            "schedules": (OnCallPageScheduledActionRelationshipsSchedules,),
            "users": (OnCallPageScheduledActionRelationshipsUsers,),
        }

    attribute_map = {
        "schedules": "schedules",
        "users": "users",
    }

    def __init__(
        self_,
        schedules: Union[OnCallPageScheduledActionRelationshipsSchedules, UnsetType] = unset,
        users: Union[OnCallPageScheduledActionRelationshipsUsers, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships of a scheduled action.

        :param schedules: The schedules the action escalates to.
        :type schedules: OnCallPageScheduledActionRelationshipsSchedules, optional

        :param users: The users the action escalates to.
        :type users: OnCallPageScheduledActionRelationshipsUsers, optional
        """
        if schedules is not unset:
            kwargs["schedules"] = schedules
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)
