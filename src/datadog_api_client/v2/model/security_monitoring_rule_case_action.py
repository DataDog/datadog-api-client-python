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
    from datadog_api_client.v2.model.security_monitoring_rule_case_action_options import (
        SecurityMonitoringRuleCaseActionOptions,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_case_action_type import (
        SecurityMonitoringRuleCaseActionType,
    )


class SecurityMonitoringRuleCaseAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case_action_options import (
            SecurityMonitoringRuleCaseActionOptions,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_case_action_type import (
            SecurityMonitoringRuleCaseActionType,
        )

        return {
            "options": (SecurityMonitoringRuleCaseActionOptions,),
            "type": (SecurityMonitoringRuleCaseActionType,),
        }

    attribute_map = {
        "options": "options",
        "type": "type",
    }

    def __init__(
        self_,
        options: Union[SecurityMonitoringRuleCaseActionOptions, UnsetType] = unset,
        type: Union[SecurityMonitoringRuleCaseActionType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Action to perform when a signal is triggered. Only available for Application Security rule type.

        :param options: Options for the rule action
        :type options: SecurityMonitoringRuleCaseActionOptions, optional

        :param type: The action type.
        :type type: SecurityMonitoringRuleCaseActionType, optional
        """
        if options is not unset:
            kwargs["options"] = options
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
