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


class ScriptDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "src": (str,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "src": "src",
        "type": "type",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        src: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ScriptDataAttributes`` object.

        :param name: The ``attributes`` ``name``.
        :type name: str, optional

        :param src: The ``attributes`` ``src``.
        :type src: str, optional

        :param type: The ``attributes`` ``type``.
        :type type: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if src is not unset:
            kwargs["src"] = src
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
