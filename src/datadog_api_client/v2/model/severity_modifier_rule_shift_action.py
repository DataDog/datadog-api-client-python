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
    from datadog_api_client.v2.model.severity_modifier_severity_delta import SeverityModifierSeverityDelta
    from datadog_api_client.v2.model.severity_modifier_rule_shift_action_type import SeverityModifierRuleShiftActionType


class SeverityModifierRuleShiftAction(ModelNormal):
    validations = {
        "description": {
            "max_length": 20000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_modifier_severity_delta import SeverityModifierSeverityDelta
        from datadog_api_client.v2.model.severity_modifier_rule_shift_action_type import (
            SeverityModifierRuleShiftActionType,
        )

        return {
            "description": (str,),
            "severity_delta": (SeverityModifierSeverityDelta,),
            "type": (SeverityModifierRuleShiftActionType,),
        }

    attribute_map = {
        "description": "description",
        "severity_delta": "severity_delta",
        "type": "type",
    }

    def __init__(
        self_,
        severity_delta: SeverityModifierSeverityDelta,
        type: SeverityModifierRuleShiftActionType,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Shifts matched findings up or down by one severity rank.

        :param description: An optional free-form explanation for the severity change.
        :type description: str, optional

        :param severity_delta: The direction in which to shift the severity of matched findings by one rank.
        :type severity_delta: SeverityModifierSeverityDelta

        :param type: The type of a severity modifier rule action that shifts the severity by one rank.
        :type type: SeverityModifierRuleShiftActionType
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.severity_delta = severity_delta
        self_.type = type
