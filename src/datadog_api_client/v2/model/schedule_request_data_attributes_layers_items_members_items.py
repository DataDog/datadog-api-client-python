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
    from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items_user import (
        ScheduleRequestDataAttributesLayersItemsMembersItemsUser,
    )


class ScheduleRequestDataAttributesLayersItemsMembersItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_request_data_attributes_layers_items_members_items_user import (
            ScheduleRequestDataAttributesLayersItemsMembersItemsUser,
        )

        return {
            "user": (ScheduleRequestDataAttributesLayersItemsMembersItemsUser,),
        }

    attribute_map = {
        "user": "user",
    }

    def __init__(
        self_, user: Union[ScheduleRequestDataAttributesLayersItemsMembersItemsUser, UnsetType] = unset, **kwargs
    ):
        """
        Defines a single member within a schedule layer, including the reference to the underlying user.

        :param user: Identifies the user participating in this layer as a single object with an ``id``.
        :type user: ScheduleRequestDataAttributesLayersItemsMembersItemsUser, optional
        """
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
