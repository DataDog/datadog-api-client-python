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


class SyntheticsTestResultDevicePlatform(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "name": "name",
        "version": "version",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, version: Union[str, UnsetType] = unset, **kwargs):
        """
        Platform information for the device used to run the test.

        :param name: Platform name (for example, ``linux`` , ``macos`` ).
        :type name: str, optional

        :param version: Platform version.
        :type version: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
