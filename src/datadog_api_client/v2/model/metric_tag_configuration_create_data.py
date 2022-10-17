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
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes
from datadog_api_client.v2.model.metric_tag_configuration_create_attributes import (
    MetricTagConfigurationCreateAttributes,
)
from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType


@dataclass
class MetricTagConfigurationCreateDataJSON:
    id: str
    aggregations: Union[MetricCustomAggregations, UnsetType] = unset
    include_percentiles: Union[bool, UnsetType] = unset
    metric_type: Union[MetricTagConfigurationMetricTypes, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class MetricTagConfigurationCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

        return {
            "attributes": (MetricTagConfigurationCreateAttributes,),
            "id": (str,),
            "type": (MetricTagConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = MetricTagConfigurationCreateDataJSON

    def __init__(
        self_,
        id: str,
        type: MetricTagConfigurationType,
        attributes: Union[MetricTagConfigurationCreateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single metric to be configure tags on.

        :param attributes: Object containing the definition of a metric tag configuration to be created.
        :type attributes: MetricTagConfigurationCreateAttributes, optional

        :param id: The metric name for this resource.
        :type id: str

        :param type: The metric tag configuration resource type.
        :type type: MetricTagConfigurationType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
