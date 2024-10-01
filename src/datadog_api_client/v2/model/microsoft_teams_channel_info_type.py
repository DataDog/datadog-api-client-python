# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MicrosoftTeamsChannelInfoType(ModelSimple):
    """
    Channel info resource type.

    :param value: If omitted defaults to "ms-teams-channel-info". Must be one of ["ms-teams-channel-info"].
    :type value: str
    """

    allowed_values = {
        "ms-teams-channel-info",
    }
    MS_TEAMS_CHANNEL_INFO: ClassVar["MicrosoftTeamsChannelInfoType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MicrosoftTeamsChannelInfoType.MS_TEAMS_CHANNEL_INFO = MicrosoftTeamsChannelInfoType("ms-teams-channel-info")
