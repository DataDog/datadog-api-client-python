# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.external_team_permission_setting_defaults_data import (
        ExternalTeamPermissionSettingDefaultsData,
    )


class ExternalTeamPermissionSettingDefaultsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.external_team_permission_setting_defaults_data import (
            ExternalTeamPermissionSettingDefaultsData,
        )

        return {
            "data": ([ExternalTeamPermissionSettingDefaultsData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[ExternalTeamPermissionSettingDefaultsData], **kwargs):
        """
        Response containing a list of external team permission setting defaults.

        :param data: A list of external team permission setting default resources.
        :type data: [ExternalTeamPermissionSettingDefaultsData]
        """
        super().__init__(kwargs)

        self_.data = data
