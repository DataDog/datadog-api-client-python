# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentGoogleChatConfigurationType(ModelSimple):
    """
    Google Chat configuration resource type.

    :param value: If omitted defaults to "google_chat_configurations". Must be one of ["google_chat_configurations"].
    :type value: str
    """

    allowed_values = {
        "google_chat_configurations",
    }
    GOOGLE_CHAT_CONFIGURATIONS: ClassVar["IncidentGoogleChatConfigurationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentGoogleChatConfigurationType.GOOGLE_CHAT_CONFIGURATIONS = IncidentGoogleChatConfigurationType(
    "google_chat_configurations"
)
