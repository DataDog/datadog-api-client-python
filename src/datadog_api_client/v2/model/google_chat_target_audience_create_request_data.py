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
    from datadog_api_client.v2.model.google_chat_target_audience_create_request_attributes import (
        GoogleChatTargetAudienceCreateRequestAttributes,
    )
    from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType


class GoogleChatTargetAudienceCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_target_audience_create_request_attributes import (
            GoogleChatTargetAudienceCreateRequestAttributes,
        )
        from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType

        return {
            "attributes": (GoogleChatTargetAudienceCreateRequestAttributes,),
            "type": (GoogleChatTargetAudienceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: GoogleChatTargetAudienceCreateRequestAttributes, type: GoogleChatTargetAudienceType, **kwargs
    ):
        """
        Data for a create target audience request.

        :param attributes: Attributes for creating a Google Chat target audience.
        :type attributes: GoogleChatTargetAudienceCreateRequestAttributes

        :param type: Google Chat target audience resource type.
        :type type: GoogleChatTargetAudienceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
