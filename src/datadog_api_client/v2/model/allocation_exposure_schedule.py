# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.allocation_exposure_guardrail_trigger import AllocationExposureGuardrailTrigger
    from datadog_api_client.v2.model.rollout_options import RolloutOptions
    from datadog_api_client.v2.model.allocation_exposure_rollout_step import AllocationExposureRolloutStep


class AllocationExposureSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.allocation_exposure_guardrail_trigger import AllocationExposureGuardrailTrigger
        from datadog_api_client.v2.model.rollout_options import RolloutOptions
        from datadog_api_client.v2.model.allocation_exposure_rollout_step import AllocationExposureRolloutStep

        return {
            "absolute_start_time": (datetime, none_type),
            "allocation_id": (UUID,),
            "control_variant_id": (str, none_type),
            "created_at": (datetime,),
            "guardrail_triggered_action": (str, none_type),
            "guardrail_triggers": ([AllocationExposureGuardrailTrigger],),
            "id": (UUID,),
            "rollout_options": (RolloutOptions,),
            "rollout_steps": ([AllocationExposureRolloutStep],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "absolute_start_time": "absolute_start_time",
        "allocation_id": "allocation_id",
        "control_variant_id": "control_variant_id",
        "created_at": "created_at",
        "guardrail_triggered_action": "guardrail_triggered_action",
        "guardrail_triggers": "guardrail_triggers",
        "id": "id",
        "rollout_options": "rollout_options",
        "rollout_steps": "rollout_steps",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        allocation_id: UUID,
        created_at: datetime,
        guardrail_triggers: List[AllocationExposureGuardrailTrigger],
        rollout_options: RolloutOptions,
        rollout_steps: List[AllocationExposureRolloutStep],
        updated_at: datetime,
        absolute_start_time: Union[datetime, none_type, UnsetType] = unset,
        control_variant_id: Union[str, none_type, UnsetType] = unset,
        guardrail_triggered_action: Union[str, none_type, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Progressive release details for a targeting rule allocation.

        :param absolute_start_time: The absolute UTC start time for this schedule.
        :type absolute_start_time: datetime, none_type, optional

        :param allocation_id: The targeting rule allocation ID this progressive rollout belongs to.
        :type allocation_id: UUID

        :param control_variant_id: The control variant ID used for experiment comparisons.
        :type control_variant_id: str, none_type, optional

        :param created_at: The timestamp when the schedule was created.
        :type created_at: datetime

        :param guardrail_triggered_action: Last guardrail action triggered for this schedule.
        :type guardrail_triggered_action: str, none_type, optional

        :param guardrail_triggers: Guardrail trigger records for this schedule.
        :type guardrail_triggers: [AllocationExposureGuardrailTrigger]

        :param id: The unique identifier of the progressive rollout.
        :type id: UUID, optional

        :param rollout_options: Applied progression options for a progressive rollout.
        :type rollout_options: RolloutOptions

        :param rollout_steps: Ordered progression steps for exposure.
        :type rollout_steps: [AllocationExposureRolloutStep]

        :param updated_at: The timestamp when the schedule was last updated.
        :type updated_at: datetime
        """
        if absolute_start_time is not unset:
            kwargs["absolute_start_time"] = absolute_start_time
        if control_variant_id is not unset:
            kwargs["control_variant_id"] = control_variant_id
        if guardrail_triggered_action is not unset:
            kwargs["guardrail_triggered_action"] = guardrail_triggered_action
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.allocation_id = allocation_id
        self_.created_at = created_at
        self_.guardrail_triggers = guardrail_triggers
        self_.rollout_options = rollout_options
        self_.rollout_steps = rollout_steps
        self_.updated_at = updated_at
