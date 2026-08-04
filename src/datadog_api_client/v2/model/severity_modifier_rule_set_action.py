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
    from datadog_api_client.v2.model.severity_modifier_severity import SeverityModifierSeverity
    from datadog_api_client.v2.model.severity_modifier_rule_set_action_type import SeverityModifierRuleSetActionType


class SeverityModifierRuleSetAction(ModelNormal):
    validations = {
        "description": {
            "max_length": 20000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_modifier_severity import SeverityModifierSeverity
        from datadog_api_client.v2.model.severity_modifier_rule_set_action_type import SeverityModifierRuleSetActionType

        return {
            "description": (str,),
            "severity": (SeverityModifierSeverity,),
            "type": (SeverityModifierRuleSetActionType,),
        }

    attribute_map = {
        "description": "description",
        "severity": "severity",
        "type": "type",
    }

    def __init__(
        self_,
        severity: SeverityModifierSeverity,
        type: SeverityModifierRuleSetActionType,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sets matched findings to a fixed severity.

        :param description: An optional free-form explanation for the severity change.
        :type description: str, optional

        :param severity: The severity to assign to matched findings. ``info_none`` is not supported for the ``iac_misconfiguration`` , ``runtime_code_vulnerability`` , ``secret`` , or ``static_code_vulnerability`` finding types.
        :type severity: SeverityModifierSeverity

        :param type: The type of a severity modifier rule action that sets a fixed severity.
        :type type: SeverityModifierRuleSetActionType
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.severity = severity
        self_.type = type
