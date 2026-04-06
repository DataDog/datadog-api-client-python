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
    from datadog_api_client.v2.model.rollout_options_request import RolloutOptionsRequest
    from datadog_api_client.v2.model.exposure_rollout_step_request import ExposureRolloutStepRequest


class ExposureScheduleRequest(ModelNormal):
    validations = {
        "rollout_steps": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rollout_options_request import RolloutOptionsRequest
        from datadog_api_client.v2.model.exposure_rollout_step_request import ExposureRolloutStepRequest

        return {
            "absolute_start_time": (datetime, none_type),
            "control_variant_id": (str, none_type),
            "control_variant_key": (str, none_type),
            "id": (UUID,),
            "rollout_options": (RolloutOptionsRequest,),
            "rollout_steps": ([ExposureRolloutStepRequest],),
        }

    attribute_map = {
        "absolute_start_time": "absolute_start_time",
        "control_variant_id": "control_variant_id",
        "control_variant_key": "control_variant_key",
        "id": "id",
        "rollout_options": "rollout_options",
        "rollout_steps": "rollout_steps",
    }

    def __init__(
        self_,
        rollout_options: RolloutOptionsRequest,
        rollout_steps: List[ExposureRolloutStepRequest],
        absolute_start_time: Union[datetime, none_type, UnsetType] = unset,
        control_variant_id: Union[str, none_type, UnsetType] = unset,
        control_variant_key: Union[str, none_type, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Progressive release request payload.

        :param absolute_start_time: The absolute UTC start time for this schedule.
        :type absolute_start_time: datetime, none_type, optional

        :param control_variant_id: The control variant ID used for experiment comparisons.
        :type control_variant_id: str, none_type, optional

        :param control_variant_key: The control variant key used during creation workflows.
        :type control_variant_key: str, none_type, optional

        :param id: The unique identifier of the progressive rollout.
        :type id: UUID, optional

        :param rollout_options: Rollout options request payload.
        :type rollout_options: RolloutOptionsRequest

        :param rollout_steps: Ordered progression steps for exposure.
        :type rollout_steps: [ExposureRolloutStepRequest]
        """
        if absolute_start_time is not unset:
            kwargs["absolute_start_time"] = absolute_start_time
        if control_variant_id is not unset:
            kwargs["control_variant_id"] = control_variant_id
        if control_variant_key is not unset:
            kwargs["control_variant_key"] = control_variant_key
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.rollout_options = rollout_options
        self_.rollout_steps = rollout_steps
