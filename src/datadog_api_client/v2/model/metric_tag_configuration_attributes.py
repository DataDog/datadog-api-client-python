# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
    from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes


class MetricTagConfigurationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
        from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

        return {
            "aggregations": (MetricCustomAggregations,),
            "created_at": (datetime,),
            "exclude_tags_mode": (bool,),
            "include_percentiles": (bool,),
            "metric_type": (MetricTagConfigurationMetricTypes,),
            "modified_at": (datetime,),
            "tags": ([str],),
        }

    attribute_map = {
        "aggregations": "aggregations",
        "created_at": "created_at",
        "exclude_tags_mode": "exclude_tags_mode",
        "include_percentiles": "include_percentiles",
        "metric_type": "metric_type",
        "modified_at": "modified_at",
        "tags": "tags",
    }

    def __init__(
        self_,
        aggregations: Union[MetricCustomAggregations, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        exclude_tags_mode: Union[bool, UnsetType] = unset,
        include_percentiles: Union[bool, UnsetType] = unset,
        metric_type: Union[MetricTagConfigurationMetricTypes, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the definition of a metric tag configuration attributes.

        :param aggregations: Deprecated. You no longer need to configure specific time and space aggregations for Metrics Without Limits.
        :type aggregations: MetricCustomAggregations, optional

        :param created_at: Timestamp when the tag configuration was created.
        :type created_at: datetime, optional

        :param exclude_tags_mode: When set to true, the configuration will exclude the configured tags and include any other submitted tags.
            When set to false, the configuration will include the configured tags and exclude any other submitted tags.
            Defaults to false. Requires ``tags`` property.
        :type exclude_tags_mode: bool, optional

        :param include_percentiles: Toggle to include or exclude percentile aggregations for distribution metrics.
            Only present when the ``metric_type`` is ``distribution``.
        :type include_percentiles: bool, optional

        :param metric_type: The metric's type.
        :type metric_type: MetricTagConfigurationMetricTypes, optional

        :param modified_at: Timestamp when the tag configuration was last modified.
        :type modified_at: datetime, optional

        :param tags: List of tag keys on which to group.
        :type tags: [str], optional
        """
        if aggregations is not unset:
            kwargs["aggregations"] = aggregations
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if exclude_tags_mode is not unset:
            kwargs["exclude_tags_mode"] = exclude_tags_mode
        if include_percentiles is not unset:
            kwargs["include_percentiles"] = include_percentiles
        if metric_type is not unset:
            kwargs["metric_type"] = metric_type
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
