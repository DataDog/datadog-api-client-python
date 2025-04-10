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


class SecurityMonitoringRuleCaseActionOptions(ModelNormal):
    validations = {
        "duration": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "duration": (int,),
            "user_behavior_name": (str,),
        }

    attribute_map = {
        "duration": "duration",
        "user_behavior_name": "userBehaviorName",
    }

    def __init__(
        self_, duration: Union[int, UnsetType] = unset, user_behavior_name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Options for the rule action

        :param duration: Duration of the action in seconds. 0 indicates no expiration.
        :type duration: int, optional

        :param user_behavior_name: Used with the case action of type 'user_behavior'. The value specified in this field is applied as a risk tag to all users affected by the rule.
        :type user_behavior_name: str, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        if user_behavior_name is not unset:
            kwargs["user_behavior_name"] = user_behavior_name
        super().__init__(kwargs)
