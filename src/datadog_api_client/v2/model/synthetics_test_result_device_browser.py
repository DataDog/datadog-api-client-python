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


class SyntheticsTestResultDeviceBrowser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "type": (str,),
            "user_agent": (str,),
            "version": (str,),
        }

    attribute_map = {
        "type": "type",
        "user_agent": "user_agent",
        "version": "version",
    }

    def __init__(
        self_,
        type: Union[str, UnsetType] = unset,
        user_agent: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Browser information for the device used to run the test.

        :param type: Browser type (for example, ``chrome`` , ``firefox`` ).
        :type type: str, optional

        :param user_agent: User agent string reported by the browser.
        :type user_agent: str, optional

        :param version: Browser version.
        :type version: str, optional
        """
        if type is not unset:
            kwargs["type"] = type
        if user_agent is not unset:
            kwargs["user_agent"] = user_agent
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
