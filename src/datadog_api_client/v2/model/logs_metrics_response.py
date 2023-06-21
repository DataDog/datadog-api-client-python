# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.logs_metric_response_data import LogsMetricResponseData
    from datadog_api_client.v2.model.logs_metric_response_compute import LogsMetricResponseCompute
    from datadog_api_client.v2.model.logs_metric_response_filter import LogsMetricResponseFilter
    from datadog_api_client.v2.model.logs_metric_response_group_by import LogsMetricResponseGroupBy


@dataclass
class LogsMetricsResponseJSON:
    id: str
    compute: Union[LogsMetricResponseCompute, UnsetType] = unset
    filter: Union[LogsMetricResponseFilter, UnsetType] = unset
    group_by: Union[List[LogsMetricResponseGroupBy], UnsetType] = unset


class LogsMetricsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_response_data import LogsMetricResponseData

        return {
            "data": ([LogsMetricResponseData],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = LogsMetricsResponseJSON

    def __init__(self_, data: Union[List[LogsMetricResponseData], UnsetType] = unset, **kwargs):
        """
        All the available log-based metric objects.

        :param data: A list of log-based metric objects.
        :type data: [LogsMetricResponseData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
