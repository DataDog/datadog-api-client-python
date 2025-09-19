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


class SecurityMonitoringRuleSequenceDetectionStepTransition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_evaluation_window import (
            SecurityMonitoringRuleEvaluationWindow,
        )

        return {
            "child": (str,),
            "evaluation_window": (SecurityMonitoringRuleEvaluationWindow,),
            "parent": (str,),
        }

    attribute_map = {
        "child": "child",
        "evaluation_window": "evaluationWindow",
        "parent": "parent",
    }

    def __init__(
        self_,
        child: Union[str, UnsetType] = unset,
        evaluation_window: Union[SecurityMonitoringRuleEvaluationWindow, UnsetType] = unset,
        parent: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Transition from a parent step to a child step within a sequence detection rule.

        :param child: Name of the child step.
        :type child: str, optional

        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window
            and evaluates in real time. For third party detection method, this field is not used.
        :type evaluation_window: SecurityMonitoringRuleEvaluationWindow, optional

        :param parent: Name of the parent step.
        :type parent: str, optional
        """
        if child is not unset:
            kwargs["child"] = child
        if evaluation_window is not unset:
            kwargs["evaluation_window"] = evaluation_window
        if parent is not unset:
            kwargs["parent"] = parent
        super().__init__(kwargs)
