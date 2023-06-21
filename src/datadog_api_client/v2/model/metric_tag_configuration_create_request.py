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
    from datadog_api_client.v2.model.metric_tag_configuration_create_data import MetricTagConfigurationCreateData
    from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
    from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes


@dataclass
class MetricTagConfigurationCreateRequestJSON:
    id: str
    aggregations: Union[MetricCustomAggregations, UnsetType] = unset
    include_percentiles: Union[bool, UnsetType] = unset
    metric_type: Union[MetricTagConfigurationMetricTypes, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class MetricTagConfigurationCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_configuration_create_data import MetricTagConfigurationCreateData

        return {
            "data": (MetricTagConfigurationCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricTagConfigurationCreateRequestJSON

    def __init__(self_, data: MetricTagConfigurationCreateData, **kwargs):
        """
        Request object that includes the metric that you would like to configure tags for.

        :param data: Object for a single metric to be configure tags on.
        :type data: MetricTagConfigurationCreateData
        """
        super().__init__(kwargs)

        self_.data = data
