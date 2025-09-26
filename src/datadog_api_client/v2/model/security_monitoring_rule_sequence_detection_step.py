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
    from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
        SecurityMonitoringRuleEvaluationWindow,
    )


class SecurityMonitoringRuleSequenceDetectionStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
            SecurityMonitoringRuleEvaluationWindow,
        )

        return {
            "condition": (str,),
            "evaluation_window": (SecurityMonitoringRuleEvaluationWindow,),
            "name": (str,),
        }

    attribute_map = {
        "condition": "condition",
        "evaluation_window": "evaluationWindow",
        "name": "name",
    }

    def __init__(
        self_,
        condition: Union[str, UnsetType] = unset,
        evaluation_window: Union[SecurityMonitoringRuleEvaluationWindow, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Step definition for sequence detection containing the step name, condition, and evaluation window.

        :param condition: Condition referencing rule queries (e.g., ``a > 0`` ).
        :type condition: str, optional

        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window
            and evaluates in real time. For third party detection method, this field is not used.
        :type evaluation_window: SecurityMonitoringRuleEvaluationWindow, optional

        :param name: Unique name identifying the step.
        :type name: str, optional
        """
        if condition is not unset:
            kwargs["condition"] = condition
        if evaluation_window is not unset:
            kwargs["evaluation_window"] = evaluation_window
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
