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


from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy
from datadog_api_client.v2.model.logs_metric_create_attributes import LogsMetricCreateAttributes
from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy

if TYPE_CHECKING:
    from datadog_api_client.v2.model.logs_metric_type import LogsMetricType


@dataclass
class LogsMetricCreateDataJSON:
    id: str
    compute: Union[LogsMetricCompute, UnsetType] = unset
    filter: Union[LogsMetricFilter, UnsetType] = unset
    group_by: Union[List[LogsMetricGroupBy], UnsetType] = unset


class LogsMetricCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_type import LogsMetricType

        return {
            "attributes": (LogsMetricCreateAttributes,),
            "id": (str,),
            "type": (LogsMetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = LogsMetricCreateDataJSON

    def __init__(self_, attributes: LogsMetricCreateAttributes, id: str, type: LogsMetricType, **kwargs):
        """
        The new log-based metric properties.

        :param attributes: The object describing the Datadog log-based metric to create.
        :type attributes: LogsMetricCreateAttributes

        :param id: The name of the log-based metric.
        :type id: str

        :param type: The type of the resource. The value should always be logs_metrics.
        :type type: LogsMetricType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
