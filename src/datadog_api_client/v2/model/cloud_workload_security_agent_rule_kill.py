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
            "signal": (str,),
        }

    attribute_map = {
        "signal": "signal",
    }

    def __init__(self_, signal: Union[str, UnsetType] = unset, **kwargs):
        """
        Kill system call applied on the container matching the rule

        :param signal: Supported signals for the kill system call.
        :type signal: str, optional
        """
        if signal is not unset:
            kwargs["signal"] = signal
        super().__init__(kwargs)
