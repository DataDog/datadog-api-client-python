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


class SyntheticsDevice(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "height": (int,),
            "id": (str,),
            "is_mobile": (bool,),
            "name": (str,),
            "width": (int,),
        }

    attribute_map = {
        "height": "height",
        "id": "id",
        "is_mobile": "isMobile",
        "name": "name",
        "width": "width",
    }

    def __init__(
        self_, height: int, id: str, name: str, width: int, is_mobile: Union[bool, UnsetType] = unset, **kwargs
    ):
        """
        Object describing the device used to perform the Synthetic test.

        :param height: Screen height of the device.
        :type height: int

        :param id: The device ID.
        :type id: str

        :param is_mobile: Whether or not the device is a mobile.
        :type is_mobile: bool, optional

        :param name: The device name.
        :type name: str

        :param width: Screen width of the device.
        :type width: int
        """
        if is_mobile is not unset:
            kwargs["is_mobile"] = is_mobile
        super().__init__(kwargs)

        self_.height = height
        self_.id = id
        self_.name = name
        self_.width = width
