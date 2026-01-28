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


class AutoCloseInactiveCases(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "max_inactive_time_in_secs": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "max_inactive_time_in_secs": "max_inactive_time_in_secs",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        max_inactive_time_in_secs: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Auto-close inactive cases settings

        :param enabled: Whether auto-close is enabled
        :type enabled: bool, optional

        :param max_inactive_time_in_secs: Maximum inactive time in seconds before auto-closing
        :type max_inactive_time_in_secs: int, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if max_inactive_time_in_secs is not unset:
            kwargs["max_inactive_time_in_secs"] = max_inactive_time_in_secs
        super().__init__(kwargs)
