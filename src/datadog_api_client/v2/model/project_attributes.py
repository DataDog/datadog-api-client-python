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


class ProjectAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.project_columns_config import ProjectColumnsConfig
        from datadog_api_client.v2.model.project_settings import ProjectSettings

        return {
            "columns_config": (ProjectColumnsConfig,),
            "enabled_custom_case_types": ([str],),
            "key": (str,),
            "name": (str,),
            "restricted": (bool,),
            "settings": (ProjectSettings,),
        }

    attribute_map = {
        "columns_config": "columns_config",
        "enabled_custom_case_types": "enabled_custom_case_types",
        "key": "key",
        "name": "name",
        "restricted": "restricted",
        "settings": "settings",
    }

    def __init__(
        self_,
        columns_config: Union[ProjectColumnsConfig, UnsetType] = unset,
        enabled_custom_case_types: Union[List[str], UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        restricted: Union[bool, UnsetType] = unset,
        settings: Union[ProjectSettings, UnsetType] = unset,
        **kwargs,
    ):
        """
        Project attributes.

        :param columns_config: Project columns configuration.
        :type columns_config: ProjectColumnsConfig, optional

        :param enabled_custom_case_types: List of enabled custom case type IDs.
        :type enabled_custom_case_types: [str], optional

        :param key: The project's key.
        :type key: str, optional

        :param name: Project's name.
        :type name: str, optional

        :param restricted: Whether the project is restricted.
        :type restricted: bool, optional

        :param settings: Project settings.
        :type settings: ProjectSettings, optional
        """
        if columns_config is not unset:
            kwargs["columns_config"] = columns_config
        if enabled_custom_case_types is not unset:
            kwargs["enabled_custom_case_types"] = enabled_custom_case_types
        if key is not unset:
            kwargs["key"] = key
        if name is not unset:
            kwargs["name"] = name
        if restricted is not unset:
            kwargs["restricted"] = restricted
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
