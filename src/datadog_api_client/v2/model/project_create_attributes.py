# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProjectCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled_custom_case_types": ([str],),
            "key": (str,),
            "name": (str,),
            "team_uuid": (str,),
        }

    attribute_map = {
        "enabled_custom_case_types": "enabled_custom_case_types",
        "key": "key",
        "name": "name",
        "team_uuid": "team_uuid",
    }

    def __init__(
        self_,
        key: str,
        name: str,
        enabled_custom_case_types: Union[List[str], UnsetType] = unset,
        team_uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Project creation attributes

        :param enabled_custom_case_types: List of enabled custom case type IDs
        :type enabled_custom_case_types: [str], optional

        :param key: Project's key. Cannot be "CASE"
        :type key: str

        :param name: Project name
        :type name: str

        :param team_uuid: Team UUID to associate with the project
        :type team_uuid: str, optional
        """
        if enabled_custom_case_types is not unset:
            kwargs["enabled_custom_case_types"] = enabled_custom_case_types
        if team_uuid is not unset:
            kwargs["team_uuid"] = team_uuid
        super().__init__(kwargs)

        self_.key = key
        self_.name = name
