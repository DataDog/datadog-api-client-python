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


class SnowflakeQueryHistoryLogsIntegrationDataflowSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "join_query_history_with_access_history_enabled": (bool,),
            "query_history_logs_interval_min": (int,),
        }

    attribute_map = {
        "join_query_history_with_access_history_enabled": "join_query_history_with_access_history_enabled",
        "query_history_logs_interval_min": "query_history_logs_interval_min",
    }

    def __init__(
        self_,
        join_query_history_with_access_history_enabled: Union[bool, UnsetType] = unset,
        query_history_logs_interval_min: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings of the query history logs dataflow.

        :param join_query_history_with_access_history_enabled: Whether query logs are joined with Snowflake access history, which adds the objects each query read and wrote so you can follow how data is used and where it came from.
        :type join_query_history_with_access_history_enabled: bool, optional

        :param query_history_logs_interval_min: How often query history logs are collected, in minutes.
        :type query_history_logs_interval_min: int, optional
        """
        if join_query_history_with_access_history_enabled is not unset:
            kwargs["join_query_history_with_access_history_enabled"] = join_query_history_with_access_history_enabled
        if query_history_logs_interval_min is not unset:
            kwargs["query_history_logs_interval_min"] = query_history_logs_interval_min
        super().__init__(kwargs)
