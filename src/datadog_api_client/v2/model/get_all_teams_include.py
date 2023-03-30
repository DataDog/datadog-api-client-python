# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetAllTeamsInclude(ModelSimple):
    """
    Included related resources optionally requested.

    :param value: Must be one of ["team_links", "user_team_permissions"].
    :type value: str
    """

    allowed_values = {
        "team_links",
        "user_team_permissions",
    }
    TEAM_LINKS: ClassVar["GetAllTeamsInclude"]
    USER_TEAM_PERMISSIONS: ClassVar["GetAllTeamsInclude"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetAllTeamsInclude.TEAM_LINKS = GetAllTeamsInclude("team_links")
GetAllTeamsInclude.USER_TEAM_PERMISSIONS = GetAllTeamsInclude("user_team_permissions")
