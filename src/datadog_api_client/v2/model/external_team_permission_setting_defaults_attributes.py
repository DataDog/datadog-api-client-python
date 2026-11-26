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
    from datadog_api_client.v2.model.external_team_permission_setting_defaults_source import (
        ExternalTeamPermissionSettingDefaultsSource,
    )


class ExternalTeamPermissionSettingDefaultsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.external_team_permission_setting_defaults_source import (
            ExternalTeamPermissionSettingDefaultsSource,
        )

        return {
            "action": (str,),
            "source": (ExternalTeamPermissionSettingDefaultsSource,),
            "value": (str,),
        }

    attribute_map = {
        "action": "action",
        "source": "source",
        "value": "value",
    }

    def __init__(self_, action: str, source: ExternalTeamPermissionSettingDefaultsSource, value: str, **kwargs):
        """
        Attributes of an external team permission setting default.

        :param action: The permission action this default applies to.
        :type action: str

        :param source: The external integration source for the permission setting default.
        :type source: ExternalTeamPermissionSettingDefaultsSource

        :param value: The default permission value for the action.
        :type value: str
        """
        super().__init__(kwargs)

        self_.action = action
        self_.source = source
        self_.value = value
