# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MicrosoftTeamsApiHandleInfoType(ModelSimple):
    """
    Handle resource type.

    :param value: If omitted defaults to "ms-teams-handle-info". Must be one of ["ms-teams-handle-info"].
    :type value: str
    """

    allowed_values = {
        "ms-teams-handle-info",
    }
    MS_TEAMS_HANDLE_INFO: ClassVar["MicrosoftTeamsApiHandleInfoType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MicrosoftTeamsApiHandleInfoType.MS_TEAMS_HANDLE_INFO = MicrosoftTeamsApiHandleInfoType("ms-teams-handle-info")
