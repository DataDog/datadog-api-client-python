# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.metric_estimate_type import MetricEstimateType
from datadog_api_client.v2.model.metric_estimate_type import MetricEstimateType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_estimate import MetricEstimate


@dataclass
class MetricEstimateResponseJSON:
    id: str
    estimate_type: Union[MetricEstimateType, UnsetType] = unset
    estimated_at: Union[datetime, UnsetType] = unset
    estimated_output_series: Union[int, UnsetType] = unset


class MetricEstimateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_estimate import MetricEstimate

        return {
            "data": (MetricEstimate,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricEstimateResponseJSON

    def __init__(self_, data: Union[MetricEstimate, UnsetType] = unset, **kwargs):
        """
        Response object that includes metric cardinality estimates.

        :param data: Object for a metric cardinality estimate.
        :type data: MetricEstimate, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
