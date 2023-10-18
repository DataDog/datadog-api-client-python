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
    from datadog_api_client.v1.model.monitor_options_custom_schedule_recurrence import (
        MonitorOptionsCustomScheduleRecurrence,
    )


class MonitorOptionsCustomSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_options_custom_schedule_recurrence import (
            MonitorOptionsCustomScheduleRecurrence,
        )

        return {
            "recurrences": ([MonitorOptionsCustomScheduleRecurrence],),
        }

    attribute_map = {
        "recurrences": "recurrences",
    }

    def __init__(self_, recurrences: Union[List[MonitorOptionsCustomScheduleRecurrence], UnsetType] = unset, **kwargs):
        """
        Configuration options for the custom schedule. **This feature is in private beta.**

        :param recurrences: Array of custom schedule recurrences.
        :type recurrences: [MonitorOptionsCustomScheduleRecurrence], optional
        """
        if recurrences is not unset:
            kwargs["recurrences"] = recurrences
        super().__init__(kwargs)
