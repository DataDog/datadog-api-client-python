# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.guardrail_trigger_action import GuardrailTriggerAction


class GuardrailMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.guardrail_trigger_action import GuardrailTriggerAction

        return {
            "metric_id": (str,),
            "trigger_action": (GuardrailTriggerAction,),
            "triggered_by": (str, none_type),
        }

    attribute_map = {
        "metric_id": "metric_id",
        "trigger_action": "trigger_action",
        "triggered_by": "triggered_by",
    }

    def __init__(
        self_,
        metric_id: str,
        trigger_action: GuardrailTriggerAction,
        triggered_by: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Guardrail metric details.

        :param metric_id: The metric ID to monitor.
        :type metric_id: str

        :param trigger_action: Action to perform when a guardrail threshold is triggered.
        :type trigger_action: GuardrailTriggerAction

        :param triggered_by: The signal or system that triggered the action.
        :type triggered_by: str, none_type, optional
        """
        if triggered_by is not unset:
            kwargs["triggered_by"] = triggered_by
        super().__init__(kwargs)

        self_.metric_id = metric_id
        self_.trigger_action = trigger_action
