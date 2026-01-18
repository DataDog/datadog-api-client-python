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


class PatchComponentRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "position": (int,),
        }

    attribute_map = {
        "name": "name",
        "position": "position",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, position: Union[int, UnsetType] = unset, **kwargs):
        """
        The supported attributes for updating a component.

        :param name: The name of the component.
        :type name: str, optional

        :param position: The position of the component. If the component belongs to a group, the position is relative to the other components in the group.
        :type position: int, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if position is not unset:
            kwargs["position"] = position
        super().__init__(kwargs)
