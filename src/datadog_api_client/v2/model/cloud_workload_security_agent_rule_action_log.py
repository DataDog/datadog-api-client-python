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


class CloudWorkloadSecurityAgentRuleActionLog(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "level": (str,),
            "message": (str,),
        }

    attribute_map = {
        "level": "level",
        "message": "message",
    }

    def __init__(self_, level: Union[str, UnsetType] = unset, message: Union[str, UnsetType] = unset, **kwargs):
        """
        The log action applied when the rule is triggered.

        :param level: The level of the log action.
        :type level: str, optional

        :param message: The message of the log action.
        :type message: str, optional
        """
        if level is not unset:
            kwargs["level"] = level
        if message is not unset:
            kwargs["message"] = message
        super().__init__(kwargs)
