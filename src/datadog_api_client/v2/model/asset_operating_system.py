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
        }

    attribute_map = {
        "description": "description",
        "name": "name",
    }

    def __init__(self_, name: str, description: Union[str, UnsetType] = unset, **kwargs):
        """
        Asset operating system.

        :param description: Operating system version.
        :type description: str, optional

        :param name: Operating system name.
        :type name: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.name = name
