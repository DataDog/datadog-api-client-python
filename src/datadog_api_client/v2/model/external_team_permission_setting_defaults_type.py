# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExternalTeamPermissionSettingDefaultsType(ModelSimple):
    """
    Resource type for external team permission setting defaults.

    :param value: If omitted defaults to "external_team_permission_setting_defaults". Must be one of ["external_team_permission_setting_defaults"].
    :type value: str
    """

    allowed_values = {
        "external_team_permission_setting_defaults",
    }
    EXTERNAL_TEAM_PERMISSION_SETTING_DEFAULTS: ClassVar["ExternalTeamPermissionSettingDefaultsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExternalTeamPermissionSettingDefaultsType.EXTERNAL_TEAM_PERMISSION_SETTING_DEFAULTS = (
    ExternalTeamPermissionSettingDefaultsType("external_team_permission_setting_defaults")
)
