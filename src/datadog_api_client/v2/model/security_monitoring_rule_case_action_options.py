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
        }

    attribute_map = {
        "duration": "duration",
    }

    def __init__(self_, duration: Union[int, UnsetType] = unset, **kwargs):
        """
        Options for the rule action

        :param duration: Duration of the action in seconds. 0 indicates no expiration.
        :type duration: int, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        super().__init__(kwargs)
