# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_page_scheduled_action_type import OnCallPageScheduledActionType


class OnCallPageScheduledActionRelationshipData(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_scheduled_action_type import OnCallPageScheduledActionType

        return {
            "id": (str,),
            "type": (OnCallPageScheduledActionType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: OnCallPageScheduledActionType, **kwargs):
        """
        Reference to the next scheduled action on the Page.

        :param id: The ID of the scheduled action. Equal to the Page ID.
        :type id: str

        :param type: Scheduled action resource type.
        :type type: OnCallPageScheduledActionType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
