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
    from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_settings_request import (
        SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest,
    )


class SnowflakeTaskHistoryLogsIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_settings_request import (
            SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest,
        )

        return {
            "enabled": (bool,),
            "settings": (SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Execution logs for your scheduled Snowflake tasks, covering start and end time, status, and any error message.

        :param enabled: Whether Datadog collects this data. Defaults to ``false`` ; set to ``true`` to start collection.
        :type enabled: bool, optional

        :param settings: Settings of the task history logs dataflow. Only the fields provided are changed.
        :type settings: SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
