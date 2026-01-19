# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GoogleChatOrganizationHandleType(ModelSimple):
    """
    Organization handle resource type.

    :param value: If omitted defaults to "google-chat-organization-handle". Must be one of ["google-chat-organization-handle"].
    :type value: str
    """

    allowed_values = {
        "google-chat-organization-handle",
    }
    GOOGLE_CHAT_ORGANIZATION_HANDLE_TYPE: ClassVar["GoogleChatOrganizationHandleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GoogleChatOrganizationHandleType.GOOGLE_CHAT_ORGANIZATION_HANDLE_TYPE = GoogleChatOrganizationHandleType(
    "google-chat-organization-handle"
)
