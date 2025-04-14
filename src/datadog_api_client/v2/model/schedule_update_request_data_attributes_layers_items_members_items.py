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
    from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_members_items_user import (
        ScheduleUpdateRequestDataAttributesLayersItemsMembersItemsUser,
    )


class ScheduleUpdateRequestDataAttributesLayersItemsMembersItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_members_items_user import (
            ScheduleUpdateRequestDataAttributesLayersItemsMembersItemsUser,
        )

        return {
            "user": (ScheduleUpdateRequestDataAttributesLayersItemsMembersItemsUser,),
        }

    attribute_map = {
        "user": "user",
    }

    def __init__(
        self_, user: Union[ScheduleUpdateRequestDataAttributesLayersItemsMembersItemsUser, UnsetType] = unset, **kwargs
    ):
        """
        Defines a single member within a layer during an update request, referring
        to a specific user.

        :param user: Identifies the user who is assigned to this member object. Only ``id`` is required.
        :type user: ScheduleUpdateRequestDataAttributesLayersItemsMembersItemsUser, optional
        """
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
