# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.project_columns_config import ProjectColumnsConfig
    from datadog_api_client.v2.model.project_settings import ProjectSettings


class ProjectUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_columns_config import ProjectColumnsConfig
        from datadog_api_client.v2.model.project_settings import ProjectSettings

        return {
            "columns_config": (ProjectColumnsConfig,),
            "enabled_custom_case_types": ([str],),
            "name": (str,),
            "settings": (ProjectSettings,),
            "team_uuid": (str,),
        }

    attribute_map = {
        "columns_config": "columns_config",
        "enabled_custom_case_types": "enabled_custom_case_types",
        "name": "name",
        "settings": "settings",
        "team_uuid": "team_uuid",
    }

    def __init__(
        self_,
        columns_config: Union[ProjectColumnsConfig, UnsetType] = unset,
        enabled_custom_case_types: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[ProjectSettings, UnsetType] = unset,
        team_uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Project update attributes

        :param columns_config: Project columns configuration
        :type columns_config: ProjectColumnsConfig, optional

        :param enabled_custom_case_types: List of enabled custom case type IDs
        :type enabled_custom_case_types: [str], optional

        :param name: Project name
        :type name: str, optional

        :param settings: Project settings
        :type settings: ProjectSettings, optional

        :param team_uuid: Team UUID to associate with the project
        :type team_uuid: str, optional
        """
        if columns_config is not unset:
            kwargs["columns_config"] = columns_config
        if enabled_custom_case_types is not unset:
            kwargs["enabled_custom_case_types"] = enabled_custom_case_types
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        if team_uuid is not unset:
            kwargs["team_uuid"] = team_uuid
        super().__init__(kwargs)
