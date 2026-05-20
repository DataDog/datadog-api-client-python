# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class SecurityMonitoringRuleImpossibleTravelOptions(ModelNormal):
    validations = {
        "baseline_user_locations_duration": {
            "inclusive_maximum": 30,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "baseline_user_locations": (bool,),
            "baseline_user_locations_duration": (int,),
        }

    attribute_map = {
        "baseline_user_locations": "baselineUserLocations",
        "baseline_user_locations_duration": "baselineUserLocationsDuration",
    }

    def __init__(
        self_,
        baseline_user_locations: Union[bool, UnsetType] = unset,
        baseline_user_locations_duration: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options on impossible travel detection method.

        :param baseline_user_locations: If true, signals are suppressed for the first 24 hours. In that time, Datadog learns the user's regular
            access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access.
        :type baseline_user_locations: bool, optional

        :param baseline_user_locations_duration: The duration in days during which Datadog learns the user's regular access locations. After this period, signals are generated for accesses from unknown locations.
        :type baseline_user_locations_duration: int, none_type, optional
        """
        if baseline_user_locations is not unset:
            kwargs["baseline_user_locations"] = baseline_user_locations
        if baseline_user_locations_duration is not unset:
            kwargs["baseline_user_locations_duration"] = baseline_user_locations_duration
        super().__init__(kwargs)
