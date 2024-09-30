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


class DeviceAttributesInterfaceStatuses(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "down": (int,),
            "off": (int,),
            "up": (int,),
            "warning": (int,),
        }

    attribute_map = {
        "down": "down",
        "off": "off",
        "up": "up",
        "warning": "warning",
    }

    def __init__(
        self_,
        down: Union[int, UnsetType] = unset,
        off: Union[int, UnsetType] = unset,
        up: Union[int, UnsetType] = unset,
        warning: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Count of the device interfaces by status

        :param down: The number of interfaces that are down
        :type down: int, optional

        :param off: The number of interfaces that are off
        :type off: int, optional

        :param up: The number of interfaces that are up
        :type up: int, optional

        :param warning: The number of interfaces that are in a warning state
        :type warning: int, optional
        """
        if down is not unset:
            kwargs["down"] = down
        if off is not unset:
            kwargs["off"] = off
        if up is not unset:
            kwargs["up"] = up
        if warning is not unset:
            kwargs["warning"] = warning
        super().__init__(kwargs)
