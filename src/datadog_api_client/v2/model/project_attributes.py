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


class ProjectAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "name": (str,),
        }

    attribute_map = {
        "key": "key",
        "name": "name",
    }

    def __init__(self_, key: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Project attributes

        :param key: The project's key
        :type key: str, optional

        :param name: Project's name
        :type name: str, optional
        """
        if key is not unset:
            kwargs["key"] = key
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
