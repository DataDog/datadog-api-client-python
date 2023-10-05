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
    from datadog_api_client.v1.model.monitor_options_custom_schedule import MonitorOptionsCustomSchedule
    from datadog_api_client.v1.model.monitor_options_scheduling_options_evaluation_window import (
        MonitorOptionsSchedulingOptionsEvaluationWindow,
    )


class MonitorOptionsSchedulingOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_options_custom_schedule import MonitorOptionsCustomSchedule
        from datadog_api_client.v1.model.monitor_options_scheduling_options_evaluation_window import (
            MonitorOptionsSchedulingOptionsEvaluationWindow,
        )

        return {
            "custom_schedule": (MonitorOptionsCustomSchedule,),
            "evaluation_window": (MonitorOptionsSchedulingOptionsEvaluationWindow,),
        }

    attribute_map = {
        "custom_schedule": "custom_schedule",
        "evaluation_window": "evaluation_window",
    }

    def __init__(
        self_,
        custom_schedule: Union[MonitorOptionsCustomSchedule, UnsetType] = unset,
        evaluation_window: Union[MonitorOptionsSchedulingOptionsEvaluationWindow, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration options for scheduling.

        :param custom_schedule: Configuration options for the custom schedule. **This feature is in private beta.**
        :type custom_schedule: MonitorOptionsCustomSchedule, optional

        :param evaluation_window: Configuration options for the evaluation window. If ``hour_starts`` is set, no other fields may be set. Otherwise, ``day_starts`` and ``month_starts`` must be set together.
        :type evaluation_window: MonitorOptionsSchedulingOptionsEvaluationWindow, optional
        """
        if custom_schedule is not unset:
            kwargs["custom_schedule"] = custom_schedule
        if evaluation_window is not unset:
            kwargs["evaluation_window"] = evaluation_window
        super().__init__(kwargs)
