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
    from datadog_api_client.v2.model.external_team_permission_setting_defaults_attributes import (
        ExternalTeamPermissionSettingDefaultsAttributes,
    )
    from datadog_api_client.v2.model.external_team_permission_setting_defaults_type import (
        ExternalTeamPermissionSettingDefaultsType,
    )


class ExternalTeamPermissionSettingDefaultsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.external_team_permission_setting_defaults_attributes import (
            ExternalTeamPermissionSettingDefaultsAttributes,
        )
        from datadog_api_client.v2.model.external_team_permission_setting_defaults_type import (
            ExternalTeamPermissionSettingDefaultsType,
        )

        return {
            "attributes": (ExternalTeamPermissionSettingDefaultsAttributes,),
            "id": (str,),
            "type": (ExternalTeamPermissionSettingDefaultsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExternalTeamPermissionSettingDefaultsAttributes,
        id: str,
        type: ExternalTeamPermissionSettingDefaultsType,
        **kwargs,
    ):
        """
        A single external team permission setting default resource.

        :param attributes: Attributes of an external team permission setting default.
        :type attributes: ExternalTeamPermissionSettingDefaultsAttributes

        :param id: The unique identifier of the external team permission setting default, formatted as ``{source}:{action}``.
        :type id: str

        :param type: Resource type for external team permission setting defaults.
        :type type: ExternalTeamPermissionSettingDefaultsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
