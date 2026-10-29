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
    from datadog_api_client.v2.model.on_call_page_scheduled_action_attributes import OnCallPageScheduledActionAttributes
    from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships import (
        OnCallPageScheduledActionRelationships,
    )
    from datadog_api_client.v2.model.on_call_page_scheduled_action_type import OnCallPageScheduledActionType


class OnCallPageScheduledAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_scheduled_action_attributes import (
            OnCallPageScheduledActionAttributes,
        )
        from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships import (
            OnCallPageScheduledActionRelationships,
        )
        from datadog_api_client.v2.model.on_call_page_scheduled_action_type import OnCallPageScheduledActionType

        return {
            "attributes": (OnCallPageScheduledActionAttributes,),
            "id": (str,),
            "relationships": (OnCallPageScheduledActionRelationships,),
            "type": (OnCallPageScheduledActionType,),
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
        type: OnCallPageScheduledActionType,
        attributes: Union[OnCallPageScheduledActionAttributes, UnsetType] = unset,
        relationships: Union[OnCallPageScheduledActionRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The next action scheduled on a Page, such as an escalation or an automatic resolution.

        :param attributes: The attributes of a scheduled action.
        :type attributes: OnCallPageScheduledActionAttributes, optional

        :param id: The ID of the scheduled action. Equal to the Page ID.
        :type id: str

        :param relationships: The relationships of a scheduled action.
        :type relationships: OnCallPageScheduledActionRelationships, optional

        :param type: Scheduled action resource type.
        :type type: OnCallPageScheduledActionType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
