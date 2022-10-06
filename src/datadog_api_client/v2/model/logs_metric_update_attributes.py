# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
    from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy


class LogsMetricUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
        from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy

        return {
            "filter": (LogsMetricFilter,),
            "group_by": ([LogsMetricGroupBy],),
        }

    attribute_map = {
        "filter": "filter",
        "group_by": "group_by",
    }

    def __init__(
        self_,
        filter: Union[LogsMetricFilter, UnsetType] = unset,
        group_by: Union[List[LogsMetricGroupBy], UnsetType] = unset,
        *args,
        **kwargs,
    ):
        """
        The log-based metric properties that will be updated.

        :param filter: The log-based metric filter. Logs matching this filter will be aggregated in this metric.
        :type filter: LogsMetricFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [LogsMetricGroupBy], optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_._check_pos_args(args)
