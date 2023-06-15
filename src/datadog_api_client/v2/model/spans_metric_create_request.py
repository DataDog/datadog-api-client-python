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


from datadog_api_client.v2.model.spans_metric_compute import SpansMetricCompute
from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy
from datadog_api_client.v2.model.spans_metric_compute import SpansMetricCompute
from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy

if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_metric_create_data import SpansMetricCreateData


@dataclass
class SpansMetricCreateRequestJSON:
    id: str
    compute: Union[SpansMetricCompute, UnsetType] = unset
    filter: Union[SpansMetricFilter, UnsetType] = unset
    group_by: Union[List[SpansMetricGroupBy], UnsetType] = unset


class SpansMetricCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_metric_create_data import SpansMetricCreateData

        return {
            "data": (SpansMetricCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SpansMetricCreateRequestJSON

    def __init__(self_, data: SpansMetricCreateData, **kwargs):
        """
        The new span-based metric body.

        :param data: The new span-based metric properties.
        :type data: SpansMetricCreateData
        """
        super().__init__(kwargs)

        self_.data = data
