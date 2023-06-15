# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes
from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_tag_configuration import MetricTagConfiguration


@dataclass
class MetricTagConfigurationResponseJSON:
    id: str
    aggregations: Union[MetricCustomAggregations, UnsetType] = unset
    created_at: Union[datetime, UnsetType] = unset
    include_percentiles: Union[bool, UnsetType] = unset
    metric_type: Union[MetricTagConfigurationMetricTypes, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class MetricTagConfigurationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_configuration import MetricTagConfiguration

        return {
            "data": (MetricTagConfiguration,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricTagConfigurationResponseJSON

    def __init__(self_, data: Union[MetricTagConfiguration, UnsetType] = unset, **kwargs):
        """
        Response object which includes a single metric's tag configuration.

        :param data: Object for a single metric tag configuration.
        :type data: MetricTagConfiguration, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
