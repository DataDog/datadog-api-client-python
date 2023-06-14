# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.team_permission_setting_serializer_action import TeamPermissionSettingSerializerAction
from datadog_api_client.v2.model.team_permission_setting_values import TeamPermissionSettingValues
from datadog_api_client.v2.model.team_permission_setting_value import TeamPermissionSettingValue
from datadog_api_client.v2.model.team_permission_setting_attributes import TeamPermissionSettingAttributes
from datadog_api_client.v2.model.team_permission_setting_serializer_action import TeamPermissionSettingSerializerAction
from datadog_api_client.v2.model.team_permission_setting_values import TeamPermissionSettingValues
from datadog_api_client.v2.model.team_permission_setting_value import TeamPermissionSettingValue

if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_permission_setting_type import TeamPermissionSettingType


@dataclass
class TeamPermissionSettingJSON:
    id: str
    action: Union[TeamPermissionSettingSerializerAction, UnsetType] = unset
    editable: Union[bool, UnsetType] = unset
    options: Union[TeamPermissionSettingValues, UnsetType] = unset
    title: Union[str, UnsetType] = unset
    value: Union[TeamPermissionSettingValue, UnsetType] = unset


class TeamPermissionSetting(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_permission_setting_type import TeamPermissionSettingType

        return {
            "attributes": (TeamPermissionSettingAttributes,),
            "id": (str,),
            "type": (TeamPermissionSettingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = TeamPermissionSettingJSON

    def __init__(
        self_,
        id: str,
        type: TeamPermissionSettingType,
        attributes: Union[TeamPermissionSettingAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team permission setting

        :param attributes: Team permission setting attributes
        :type attributes: TeamPermissionSettingAttributes, optional

        :param id: The team permission setting's identifier
        :type id: str

        :param type: Team permission setting type
        :type type: TeamPermissionSettingType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
