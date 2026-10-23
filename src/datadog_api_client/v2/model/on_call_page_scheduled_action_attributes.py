# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_page_scheduled_action_attributes_type import (
        OnCallPageScheduledActionAttributesType,
    )


class OnCallPageScheduledActionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_scheduled_action_attributes_type import (
            OnCallPageScheduledActionAttributesType,
        )

        return {
            "at": (datetime,),
            "type": (OnCallPageScheduledActionAttributesType,),
        }

    attribute_map = {
        "at": "at",
        "type": "type",
    }

    def __init__(
        self_,
        at: Union[datetime, UnsetType] = unset,
        type: Union[OnCallPageScheduledActionAttributesType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a scheduled action.

        :param at: The time when the action is scheduled to run.
        :type at: datetime, optional

        :param type: The kind of action that is scheduled.
        :type type: OnCallPageScheduledActionAttributesType, optional
        """
        if at is not unset:
            kwargs["at"] = at
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
