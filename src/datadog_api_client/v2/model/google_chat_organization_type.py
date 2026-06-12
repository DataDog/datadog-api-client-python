# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GoogleChatOrganizationType(ModelSimple):
    """
    Google Chat organization resource type.

    :param value: If omitted defaults to "google-chat-organization". Must be one of ["google-chat-organization"].
    :type value: str
    """

    allowed_values = {
        "google-chat-organization",
    }
    GOOGLE_CHAT_ORGANIZATION_TYPE: ClassVar["GoogleChatOrganizationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GoogleChatOrganizationType.GOOGLE_CHAT_ORGANIZATION_TYPE = GoogleChatOrganizationType("google-chat-organization")
