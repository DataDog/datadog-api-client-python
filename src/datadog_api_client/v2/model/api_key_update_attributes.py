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


class APIKeyUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "name": (str,),
            "remote_config_read_enabled": (bool,),
        }

    attribute_map = {
        "category": "category",
        "name": "name",
        "remote_config_read_enabled": "remote_config_read_enabled",
    }

    def __init__(
        self_,
        name: str,
        category: Union[str, UnsetType] = unset,
        remote_config_read_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to update an API Key.

        :param category: The APIKeyUpdateAttributes category.
        :type category: str, optional

        :param name: Name of the API key.
        :type name: str

        :param remote_config_read_enabled: The APIKeyUpdateAttributes remote_config_read_enabled.
        :type remote_config_read_enabled: bool, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if remote_config_read_enabled is not unset:
            kwargs["remote_config_read_enabled"] = remote_config_read_enabled
        super().__init__(kwargs)

        self_.name = name
