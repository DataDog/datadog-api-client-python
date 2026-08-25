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


class AssetOperatingSystem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "version": "version",
    }

    def __init__(
        self_, name: str, description: Union[str, UnsetType] = unset, version: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Asset operating system.

        :param description: Operating system version.
        :type description: str, optional

        :param name: Operating system name.
        :type name: str

        :param version: Operating system version.
        :type version: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.name = name
