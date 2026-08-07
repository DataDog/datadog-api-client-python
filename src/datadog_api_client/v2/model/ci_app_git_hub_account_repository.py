# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CIAppGitHubAccountRepository(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "name": "name",
    }

    def __init__(self_, enabled: Union[bool, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        A GitHub repository within a GitHub account, and its CI Visibility opt-in status.

        :param enabled: Whether CI Visibility is enabled for this repository.
        :type enabled: bool, optional

        :param name: The repository name.
        :type name: str, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
