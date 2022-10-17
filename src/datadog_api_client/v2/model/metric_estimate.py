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
from datadog_api_client.v2.model.metric_estimate_attributes import MetricEstimateAttributes
from datadog_api_client.v2.model.metric_estimate_type import MetricEstimateType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_estimate_resource_type import MetricEstimateResourceType


@dataclass
class MetricEstimateJSON:
    id: str
    estimate_type: Union[MetricEstimateType, UnsetType] = unset
    estimated_at: Union[datetime, UnsetType] = unset
    estimated_output_series: Union[int, UnsetType] = unset


class MetricEstimate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_estimate_resource_type import MetricEstimateResourceType

        return {
            "attributes": (MetricEstimateAttributes,),
            "id": (str,),
            "type": (MetricEstimateResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = MetricEstimateJSON

    def __init__(
        self_,
        attributes: Union[MetricEstimateAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[MetricEstimateResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a metric cardinality estimate.

        :param attributes: Object containing the definition of a metric estimate attribute.
        :type attributes: MetricEstimateAttributes, optional

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric estimate resource type.
        :type type: MetricEstimateResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
