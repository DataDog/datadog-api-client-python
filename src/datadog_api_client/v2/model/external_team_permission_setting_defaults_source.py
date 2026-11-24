# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExternalTeamPermissionSettingDefaultsSource(ModelSimple):
    """
    The external integration source for the permission setting default.

    :param value: Must be one of ["github", "scim", "servicenow"].
    :type value: str
    """

    allowed_values = {
        "github",
        "scim",
        "servicenow",
    }
    GITHUB: ClassVar["ExternalTeamPermissionSettingDefaultsSource"]
    SCIM: ClassVar["ExternalTeamPermissionSettingDefaultsSource"]
    SERVICENOW: ClassVar["ExternalTeamPermissionSettingDefaultsSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExternalTeamPermissionSettingDefaultsSource.GITHUB = ExternalTeamPermissionSettingDefaultsSource("github")
ExternalTeamPermissionSettingDefaultsSource.SCIM = ExternalTeamPermissionSettingDefaultsSource("scim")
ExternalTeamPermissionSettingDefaultsSource.SERVICENOW = ExternalTeamPermissionSettingDefaultsSource("servicenow")
