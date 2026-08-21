# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_retention_quota_reached_action import RumRetentionQuotaReachedAction
    from datadog_api_client.v2.model.rum_retention_quota_window_type import RumRetentionQuotaWindowType


class RumRetentionQuotaCustomConfig(ModelNormal):
    validations = {
        "daily_reset_time": {},
        "daily_reset_timezone": {},
        "session_limit": {
            "inclusive_minimum": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_quota_reached_action import RumRetentionQuotaReachedAction
        from datadog_api_client.v2.model.rum_retention_quota_window_type import RumRetentionQuotaWindowType

        return {
            "daily_reset_time": (str,),
            "daily_reset_timezone": (str,),
            "quota_reached_action": (RumRetentionQuotaReachedAction,),
            "session_limit": (int,),
            "window_type": (RumRetentionQuotaWindowType,),
        }

    attribute_map = {
        "daily_reset_time": "daily_reset_time",
        "daily_reset_timezone": "daily_reset_timezone",
        "quota_reached_action": "quota_reached_action",
        "session_limit": "session_limit",
        "window_type": "window_type",
    }

    def __init__(
        self_,
        daily_reset_time: str,
        daily_reset_timezone: str,
        quota_reached_action: RumRetentionQuotaReachedAction,
        session_limit: int,
        window_type: RumRetentionQuotaWindowType,
        **kwargs,
    ):
        """
        The configuration used when ``mode`` is ``custom``.

        :param daily_reset_time: The time of day when the daily quota resets, in ``HH:MM`` 24-hour format.
        :type daily_reset_time: str

        :param daily_reset_timezone: The timezone offset used for the daily reset time, in ``±HH:MM`` format.
        :type daily_reset_timezone: str

        :param quota_reached_action: The action to take when the session quota is reached.
        :type quota_reached_action: RumRetentionQuotaReachedAction

        :param session_limit: The maximum number of sessions allowed within the window. Must be at least ``1000``.
        :type session_limit: int

        :param window_type: The window type over which the session limit is enforced.
        :type window_type: RumRetentionQuotaWindowType
        """
        super().__init__(kwargs)

        self_.daily_reset_time = daily_reset_time
        self_.daily_reset_timezone = daily_reset_timezone
        self_.quota_reached_action = quota_reached_action
        self_.session_limit = session_limit
        self_.window_type = window_type
