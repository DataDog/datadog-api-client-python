# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_protocol_exposure_step_input import (
        ExperimentsProtocolExposureStepInput,
    )


class ExperimentsPatchProtocolExposureScheduleInput(ModelNormal):
    validations = {
        "selection_interval_ms": {
            "inclusive_minimum": 0,
        },
    }
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_protocol_exposure_step_input import (
            ExperimentsProtocolExposureStepInput,
        )

        return {
            "autostart": (bool, none_type),
            "guardrail_triggered_action": (str, none_type),
            "rollout_steps": ([ExperimentsProtocolExposureStepInput], none_type),
            "selection_interval_ms": (int, none_type),
            "strategy": (str, none_type),
        }

    attribute_map = {
        "autostart": "autostart",
        "guardrail_triggered_action": "guardrail_triggered_action",
        "rollout_steps": "rollout_steps",
        "selection_interval_ms": "selection_interval_ms",
        "strategy": "strategy",
    }

    def __init__(
        self_,
        autostart: Union[bool, none_type, UnsetType] = unset,
        guardrail_triggered_action: Union[str, none_type, UnsetType] = unset,
        rollout_steps: Union[List[ExperimentsProtocolExposureStepInput], none_type, UnsetType] = unset,
        selection_interval_ms: Union[int, none_type, UnsetType] = unset,
        strategy: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Partial traffic schedule. Omitted fields remain unchanged. Null clears the whole schedule. Null clears nullable fields and rollout_steps; null sets strategy to an empty string and ``autostart`` to false.

        :param autostart: Whether the exposure schedule starts automatically.
        :type autostart: bool, none_type, optional

        :param guardrail_triggered_action: Action taken when a guardrail triggers during the exposure schedule.
        :type guardrail_triggered_action: str, none_type, optional

        :param rollout_steps: Rollout steps, replaced when supplied.
        :type rollout_steps: [ExperimentsProtocolExposureStepInput], none_type, optional

        :param selection_interval_ms: Interval between traffic selections, in milliseconds.
        :type selection_interval_ms: int, none_type, optional

        :param strategy: Method used to increase traffic exposure over the schedule.
        :type strategy: str, none_type, optional
        """
        if autostart is not unset:
            kwargs["autostart"] = autostart
        if guardrail_triggered_action is not unset:
            kwargs["guardrail_triggered_action"] = guardrail_triggered_action
        if rollout_steps is not unset:
            kwargs["rollout_steps"] = rollout_steps
        if selection_interval_ms is not unset:
            kwargs["selection_interval_ms"] = selection_interval_ms
        if strategy is not unset:
            kwargs["strategy"] = strategy
        super().__init__(kwargs)
