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
    from datadog_api_client.v2.model.google_chat_target_audience_update_request_attributes import (
        GoogleChatTargetAudienceUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType


class GoogleChatTargetAudienceUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_target_audience_update_request_attributes import (
            GoogleChatTargetAudienceUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType

        return {
            "attributes": (GoogleChatTargetAudienceUpdateRequestAttributes,),
            "type": (GoogleChatTargetAudienceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: GoogleChatTargetAudienceUpdateRequestAttributes, type: GoogleChatTargetAudienceType, **kwargs
    ):
        """
        Data for an update target audience request.

        :param attributes: Attributes for updating a Google Chat target audience.
        :type attributes: GoogleChatTargetAudienceUpdateRequestAttributes

        :param type: Google Chat target audience resource type.
        :type type: GoogleChatTargetAudienceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
