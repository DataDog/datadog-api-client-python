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
    from datadog_api_client.v1.model.logs_daily_limit_reset import LogsDailyLimitReset
    from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
    from datadog_api_client.v1.model.logs_filter import LogsFilter


class LogsIndex(ModelNormal):
    validations = {
        "daily_limit_warning_threshold_percentage": {
            "inclusive_maximum": 99.99,
            "inclusive_minimum": 50,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_daily_limit_reset import LogsDailyLimitReset
        from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
        from datadog_api_client.v1.model.logs_filter import LogsFilter

        return {
            "daily_limit": (int,),
            "daily_limit_reset": (LogsDailyLimitReset,),
            "daily_limit_warning_threshold_percentage": (float,),
            "exclusion_filters": ([LogsExclusion],),
            "filter": (LogsFilter,),
            "is_rate_limited": (bool,),
            "name": (str,),
            "num_flex_logs_retention_days": (int,),
            "num_retention_days": (int,),
        }

    attribute_map = {
        "daily_limit": "daily_limit",
        "daily_limit_reset": "daily_limit_reset",
        "daily_limit_warning_threshold_percentage": "daily_limit_warning_threshold_percentage",
        "exclusion_filters": "exclusion_filters",
        "filter": "filter",
        "is_rate_limited": "is_rate_limited",
        "name": "name",
        "num_flex_logs_retention_days": "num_flex_logs_retention_days",
        "num_retention_days": "num_retention_days",
    }
    read_only_vars = {
        "is_rate_limited",
    }

    def __init__(
        self_,
        filter: LogsFilter,
        name: str,
        daily_limit: Union[int, UnsetType] = unset,
        daily_limit_reset: Union[LogsDailyLimitReset, UnsetType] = unset,
        daily_limit_warning_threshold_percentage: Union[float, UnsetType] = unset,
        exclusion_filters: Union[List[LogsExclusion], UnsetType] = unset,
        is_rate_limited: Union[bool, UnsetType] = unset,
        num_flex_logs_retention_days: Union[int, UnsetType] = unset,
        num_retention_days: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing a Datadog Log index.

        :param daily_limit: The number of log events you can send in this index per day before you are rate-limited.
        :type daily_limit: int, optional

        :param daily_limit_reset: Object containing options to override the default daily limit reset time.
        :type daily_limit_reset: LogsDailyLimitReset, optional

        :param daily_limit_warning_threshold_percentage: A percentage threshold of the daily quota at which a Datadog warning event is generated.
        :type daily_limit_warning_threshold_percentage: float, optional

        :param exclusion_filters: An array of exclusion objects. The logs are tested against the query of each filter,
            following the order of the array. Only the first matching active exclusion matters,
            others (if any) are ignored.
        :type exclusion_filters: [LogsExclusion], optional

        :param filter: Filter for logs.
        :type filter: LogsFilter

        :param is_rate_limited: A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent.
            Rate limit is reset every-day at 2pm UTC.
        :type is_rate_limited: bool, optional

        :param name: The name of the index.
        :type name: str

        :param num_flex_logs_retention_days: The total number of days logs are stored in Standard and Flex Tier before being deleted from the index.
            If Standard Tier is enabled on this index, logs are first retained in Standard Tier for the number of days specified through ``num_retention_days`` ,
            and then stored in Flex Tier until the number of days specified in ``num_flex_logs_retention_days`` is reached.
            The available values depend on retention plans specified in your organization's contract/subscriptions.
        :type num_flex_logs_retention_days: int, optional

        :param num_retention_days: The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index.
            The available values depend on retention plans specified in your organization's contract/subscriptions.
        :type num_retention_days: int, optional
        """
        if daily_limit is not unset:
            kwargs["daily_limit"] = daily_limit
        if daily_limit_reset is not unset:
            kwargs["daily_limit_reset"] = daily_limit_reset
        if daily_limit_warning_threshold_percentage is not unset:
            kwargs["daily_limit_warning_threshold_percentage"] = daily_limit_warning_threshold_percentage
        if exclusion_filters is not unset:
            kwargs["exclusion_filters"] = exclusion_filters
        if is_rate_limited is not unset:
            kwargs["is_rate_limited"] = is_rate_limited
        if num_flex_logs_retention_days is not unset:
            kwargs["num_flex_logs_retention_days"] = num_flex_logs_retention_days
        if num_retention_days is not unset:
            kwargs["num_retention_days"] = num_retention_days
        super().__init__(kwargs)

        self_.filter = filter
        self_.name = name
