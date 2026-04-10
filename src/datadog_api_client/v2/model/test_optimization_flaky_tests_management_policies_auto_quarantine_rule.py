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


class TestOptimizationFlakyTestsManagementPoliciesAutoQuarantineRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "window_seconds": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "window_seconds": "window_seconds",
    }

    def __init__(
        self_, enabled: Union[bool, UnsetType] = unset, window_seconds: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Automatic quarantine triggering rule based on a time window.

        :param enabled: Whether this auto-quarantine rule is enabled.
        :type enabled: bool, optional

        :param window_seconds: Time window in seconds over which flakiness is evaluated. Must be greater than 0.
        :type window_seconds: int, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if window_seconds is not unset:
            kwargs["window_seconds"] = window_seconds
        super().__init__(kwargs)
