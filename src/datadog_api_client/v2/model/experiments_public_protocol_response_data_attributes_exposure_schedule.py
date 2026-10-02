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
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_exposure_schedule_rollout_steps_items import (
        ExperimentsPublicProtocolResponseDataAttributesExposureScheduleRolloutStepsItems,
    )


class ExperimentsPublicProtocolResponseDataAttributesExposureSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_exposure_schedule_rollout_steps_items import (
            ExperimentsPublicProtocolResponseDataAttributesExposureScheduleRolloutStepsItems,
        )

        return {
            "autostart": (bool,),
            "guardrail_triggered_action": (str,),
            "rollout_steps": ([ExperimentsPublicProtocolResponseDataAttributesExposureScheduleRolloutStepsItems],),
            "selection_interval_ms": (int,),
            "strategy": (str,),
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
        autostart: Union[bool, UnsetType] = unset,
        guardrail_triggered_action: Union[str, UnsetType] = unset,
        rollout_steps: Union[
            List[ExperimentsPublicProtocolResponseDataAttributesExposureScheduleRolloutStepsItems], UnsetType
        ] = unset,
        selection_interval_ms: Union[int, UnsetType] = unset,
        strategy: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Schedule that controls traffic exposure for experiments created from the protocol.

        :param autostart: Whether the exposure schedule starts automatically.
        :type autostart: bool, optional

        :param guardrail_triggered_action: Action taken when a guardrail triggers during the exposure schedule.
        :type guardrail_triggered_action: str, optional

        :param rollout_steps: Ordered steps that define changes in traffic exposure.
        :type rollout_steps: [ExperimentsPublicProtocolResponseDataAttributesExposureScheduleRolloutStepsItems], optional

        :param selection_interval_ms: Interval between traffic selections, in milliseconds.
        :type selection_interval_ms: int, optional

        :param strategy: Method used to increase traffic exposure over the schedule.
        :type strategy: str, optional
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
