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


from datadog_api_client.v2.model.logs_metric_update_compute import LogsMetricUpdateCompute
from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy
from datadog_api_client.v2.model.logs_metric_update_compute import LogsMetricUpdateCompute
from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy

if TYPE_CHECKING:
    from datadog_api_client.v2.model.logs_metric_update_data import LogsMetricUpdateData


@dataclass
class LogsMetricUpdateRequestJSON:
    compute: Union[LogsMetricUpdateCompute, UnsetType] = unset
    filter: Union[LogsMetricFilter, UnsetType] = unset
    group_by: Union[List[LogsMetricGroupBy], UnsetType] = unset


class LogsMetricUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_update_data import LogsMetricUpdateData

        return {
            "data": (LogsMetricUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = LogsMetricUpdateRequestJSON

    def __init__(self_, data: LogsMetricUpdateData, **kwargs):
        """
        The new log-based metric body.

        :param data: The new log-based metric properties.
        :type data: LogsMetricUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
