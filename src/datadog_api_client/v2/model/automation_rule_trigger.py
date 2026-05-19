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
    from datadog_api_client.v2.model.automation_rule_trigger_data import AutomationRuleTriggerData
    from datadog_api_client.v2.model.automation_rule_trigger_type import AutomationRuleTriggerType


class AutomationRuleTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_trigger_data import AutomationRuleTriggerData
        from datadog_api_client.v2.model.automation_rule_trigger_type import AutomationRuleTriggerType

        return {
            "data": (AutomationRuleTriggerData,),
            "type": (AutomationRuleTriggerType,),
        }

    attribute_map = {
        "data": "data",
        "type": "type",
    }

    def __init__(
        self_, type: AutomationRuleTriggerType, data: Union[AutomationRuleTriggerData, UnsetType] = unset, **kwargs
    ):
        """
        Defines when the rule activates. Combines a trigger type (the case event to listen for) with optional trigger data (conditions that narrow when the trigger fires).

        :param data: Additional configuration for the trigger, dependent on the trigger type. For ``status_transitioned`` triggers, specify ``from_status_name`` and ``to_status_name``. For ``attribute_value_changed`` triggers, specify ``field`` and ``change_type``.
        :type data: AutomationRuleTriggerData, optional

        :param type: The case event that activates the automation rule.
        :type type: AutomationRuleTriggerType
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)

        self_.type = type
