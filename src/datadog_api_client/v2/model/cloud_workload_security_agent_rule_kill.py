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


class CloudWorkloadSecurityAgentRuleKill(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disable_container_disarmer": (bool,),
            "disable_executable_disarmer": (bool,),
            "scope": (str,),
            "signal": (str,),
        }

    attribute_map = {
        "disable_container_disarmer": "disable_container_disarmer",
        "disable_executable_disarmer": "disable_executable_disarmer",
        "scope": "scope",
        "signal": "signal",
    }

    def __init__(
        self_,
        disable_container_disarmer: Union[bool, UnsetType] = unset,
        disable_executable_disarmer: Union[bool, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        signal: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Kill system call applied on the container matching the rule

        :param disable_container_disarmer: Whether the automatic container safeguard of the kill action is disabled.
        :type disable_container_disarmer: bool, optional

        :param disable_executable_disarmer: Whether the automatic executable safeguard of the kill action is disabled.
        :type disable_executable_disarmer: bool, optional

        :param scope: The scope of the kill action.
        :type scope: str, optional

        :param signal: Supported signals for the kill system call
        :type signal: str, optional
        """
        if disable_container_disarmer is not unset:
            kwargs["disable_container_disarmer"] = disable_container_disarmer
        if disable_executable_disarmer is not unset:
            kwargs["disable_executable_disarmer"] = disable_executable_disarmer
        if scope is not unset:
            kwargs["scope"] = scope
        if signal is not unset:
            kwargs["signal"] = signal
        super().__init__(kwargs)
