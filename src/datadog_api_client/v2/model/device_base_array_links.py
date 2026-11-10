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


class DeviceBaseArrayLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next": (str,),
            "self": (str,),
        }

    attribute_map = {
        "next": "next",
        "self": "self",
    }

    def __init__(self_, next: Union[str, UnsetType] = unset, self: Union[str, UnsetType] = unset, **kwargs):
        """
        Links related to the current page of devices.

        :param next: URL of the next page of devices. Present only when more devices remain.
        :type next: str, optional

        :param self: URL of the current request.
        :type self: str, optional
        """
        if next is not unset:
            kwargs["next"] = next
        if self is not unset:
            kwargs["self"] = self
        super().__init__(kwargs)
