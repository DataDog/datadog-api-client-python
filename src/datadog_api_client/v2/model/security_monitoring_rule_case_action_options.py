# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_case_action_options_flagged_ip_type import (
        SecurityMonitoringRuleCaseActionOptionsFlaggedIPType,
    )


class SecurityMonitoringRuleCaseActionOptions(ModelNormal):
    validations = {
        "duration": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case_action_options_flagged_ip_type import (
            SecurityMonitoringRuleCaseActionOptionsFlaggedIPType,
        )

        return {
            "duration": (int,),
            "flagged_ip_type": (SecurityMonitoringRuleCaseActionOptionsFlaggedIPType,),
            "user_behavior_name": (str,),
        }

    attribute_map = {
        "duration": "duration",
        "flagged_ip_type": "flaggedIPType",
        "user_behavior_name": "userBehaviorName",
    }

    def __init__(
        self_,
        duration: Union[int, UnsetType] = unset,
        flagged_ip_type: Union[SecurityMonitoringRuleCaseActionOptionsFlaggedIPType, UnsetType] = unset,
        user_behavior_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options for the rule action

        :param duration: Duration of the action in seconds. 0 indicates no expiration.
        :type duration: int, optional

        :param flagged_ip_type: Used with the case action of type 'flag_ip'. The value specified in this field is applied as a flag to the IP addresses.
        :type flagged_ip_type: SecurityMonitoringRuleCaseActionOptionsFlaggedIPType, optional

        :param user_behavior_name: Used with the case action of type 'user_behavior'. The value specified in this field is applied as a risk tag to all users affected by the rule.
        :type user_behavior_name: str, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        if flagged_ip_type is not unset:
            kwargs["flagged_ip_type"] = flagged_ip_type
        if user_behavior_name is not unset:
            kwargs["user_behavior_name"] = user_behavior_name
        super().__init__(kwargs)
