# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class MetricTagConfigurationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
        from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

        return {
            "aggregations": (MetricCustomAggregations,),
            "created_at": (datetime,),
            "include_percentiles": (bool,),
            "metric_type": (MetricTagConfigurationMetricTypes,),
            "modified_at": (datetime,),
            "tags": ([str],),
        }

    attribute_map = {
        "aggregations": "aggregations",
        "created_at": "created_at",
        "include_percentiles": "include_percentiles",
        "metric_type": "metric_type",
        "modified_at": "modified_at",
        "tags": "tags",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing the definition of a metric tag configuration attributes.

        :param aggregations: A list of queryable aggregation combinations for a count, rate, or gauge metric.
            By default, count and rate metrics require the (time: sum, space: sum) aggregation and
            Gauge metrics require the (time: avg, space: avg) aggregation.
            Additional time & space combinations are also available:


            * time: avg, space: avg
            * time: avg, space: max
            * time: avg, space: min
            * time: avg, space: sum
            * time: count, space: sum
            * time: max, space: max
            * time: min, space: min
            * time: sum, space: avg
            * time: sum, space: sum

            Can only be applied to metrics that have a ``metric_type`` of ``count`` , ``rate`` , or ``gauge``.
        :type aggregations: MetricCustomAggregations, optional

        :param created_at: Timestamp when the tag configuration was created.
        :type created_at: datetime, optional

        :param include_percentiles: Toggle to turn on/off percentile aggregations for distribution metrics.
            Only present when the ``metric_type`` is ``distribution``.
        :type include_percentiles: bool, optional

        :param metric_type: The metric's type.
        :type metric_type: MetricTagConfigurationMetricTypes, optional

        :param modified_at: Timestamp when the tag configuration was last modified.
        :type modified_at: datetime, optional

        :param tags: List of tag keys on which to group.
        :type tags: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricTagConfigurationAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
