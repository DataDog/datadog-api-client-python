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


class CustomFrameworkWithoutRequirements(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "handle": (str,),
            "icon_url": (str,),
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "description": "description",
        "handle": "handle",
        "icon_url": "icon_url",
        "name": "name",
        "version": "version",
    }

    def __init__(
        self_,
        handle: str,
        name: str,
        version: str,
        description: Union[str, UnsetType] = unset,
        icon_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Framework without requirements.

        :param description: Framework Description
        :type description: str, optional

        :param handle: Framework Handle
        :type handle: str

        :param icon_url: Framework Icon URL
        :type icon_url: str, optional

        :param name: Framework Name
        :type name: str

        :param version: Framework Version
        :type version: str
        """
        if description is not unset:
            kwargs["description"] = description
        if icon_url is not unset:
            kwargs["icon_url"] = icon_url
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
        self_.version = version
