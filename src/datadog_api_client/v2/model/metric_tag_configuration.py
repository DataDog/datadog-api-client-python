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
from datadog_api_client.v2.model.metric_tag_configuration_attributes import MetricTagConfigurationAttributes
from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType


@dataclass
class MetricTagConfigurationJSON:
    id: str
    aggregations: Union[MetricCustomAggregations, UnsetType] = unset
    created_at: Union[datetime, UnsetType] = unset
    include_percentiles: Union[bool, UnsetType] = unset
    metric_type: Union[MetricTagConfigurationMetricTypes, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class MetricTagConfiguration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

        return {
            "attributes": (MetricTagConfigurationAttributes,),
            "id": (str,),
            "type": (MetricTagConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = MetricTagConfigurationJSON

    def __init__(
        self_,
        attributes: Union[MetricTagConfigurationAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[MetricTagConfigurationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single metric tag configuration.

        :param attributes: Object containing the definition of a metric tag configuration attributes.
        :type attributes: MetricTagConfigurationAttributes, optional

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric tag configuration resource type.
        :type type: MetricTagConfigurationType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
