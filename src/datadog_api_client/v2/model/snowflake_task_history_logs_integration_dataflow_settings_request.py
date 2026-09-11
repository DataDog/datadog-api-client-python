# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "task_history_logs_interval_min": (int,),
        }

    attribute_map = {
        "task_history_logs_interval_min": "task_history_logs_interval_min",
    }

    def __init__(self_, task_history_logs_interval_min: Union[int, UnsetType] = unset, **kwargs):
        """
        Settings of the task history logs dataflow. Only the fields provided are changed.

        :param task_history_logs_interval_min: How often task history logs are collected, in minutes. One of ``5`` , ``15`` , ``30`` , ``60`` , or ``1440``. Defaults to ``5``.
        :type task_history_logs_interval_min: int, optional
        """
        if task_history_logs_interval_min is not unset:
            kwargs["task_history_logs_interval_min"] = task_history_logs_interval_min
        super().__init__(kwargs)
