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


from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_tag_configuration_update_data import MetricTagConfigurationUpdateData


@dataclass
class MetricTagConfigurationUpdateRequestJSON:
    id: str
    aggregations: Union[MetricCustomAggregations, UnsetType] = unset
    include_percentiles: Union[bool, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class MetricTagConfigurationUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_configuration_update_data import MetricTagConfigurationUpdateData

        return {
            "data": (MetricTagConfigurationUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricTagConfigurationUpdateRequestJSON

    def __init__(self_, data: MetricTagConfigurationUpdateData, **kwargs):
        """
        Request object that includes the metric that you would like to edit the tag configuration on.

        :param data: Object for a single tag configuration to be edited.
        :type data: MetricTagConfigurationUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
