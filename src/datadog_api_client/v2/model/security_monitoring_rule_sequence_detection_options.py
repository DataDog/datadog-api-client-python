# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_sequence_detection_step_transition import (
        SecurityMonitoringRuleSequenceDetectionStepTransition,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_sequence_detection_step import (
        SecurityMonitoringRuleSequenceDetectionStep,
    )


class SecurityMonitoringRuleSequenceDetectionOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_sequence_detection_step_transition import (
            SecurityMonitoringRuleSequenceDetectionStepTransition,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_sequence_detection_step import (
            SecurityMonitoringRuleSequenceDetectionStep,
        )

        return {
            "step_transitions": ([SecurityMonitoringRuleSequenceDetectionStepTransition],),
            "steps": ([SecurityMonitoringRuleSequenceDetectionStep],),
        }

    attribute_map = {
        "step_transitions": "stepTransitions",
        "steps": "steps",
    }

    def __init__(
        self_,
        step_transitions: Union[List[SecurityMonitoringRuleSequenceDetectionStepTransition], UnsetType] = unset,
        steps: Union[List[SecurityMonitoringRuleSequenceDetectionStep], UnsetType] = unset,
        **kwargs,
    ):
        """
        Options on sequence detection method.

        :param step_transitions: Transitions defining the allowed order of steps and their evaluation windows.
        :type step_transitions: [SecurityMonitoringRuleSequenceDetectionStepTransition], optional

        :param steps: Steps that define the conditions to be matched in sequence.
        :type steps: [SecurityMonitoringRuleSequenceDetectionStep], optional
        """
        if step_transitions is not unset:
            kwargs["step_transitions"] = step_transitions
        if steps is not unset:
            kwargs["steps"] = steps
        super().__init__(kwargs)
