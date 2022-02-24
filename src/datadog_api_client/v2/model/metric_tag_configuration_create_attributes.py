# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
    from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

    globals()["MetricCustomAggregations"] = MetricCustomAggregations
    globals()["MetricTagConfigurationMetricTypes"] = MetricTagConfigurationMetricTypes


class MetricTagConfigurationCreateAttributes(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "aggregations": (MetricCustomAggregations,),
            "include_percentiles": (bool,),
            "metric_type": (MetricTagConfigurationMetricTypes,),
            "tags": ([str],),
        }

    attribute_map = {
        "aggregations": "aggregations",
        "include_percentiles": "include_percentiles",
        "metric_type": "metric_type",
        "tags": "tags",
    }

    read_only_vars = {}

    def __init__(self, metric_type, *args, **kwargs):
        """
        Object containing the definition of a metric tag configuration to be created.

        :param aggregations: A list of queryable aggregation combinations for a count, rate, or gauge metric.
            By default, count and rate metrics require the (time: sum, space: sum) aggregation and
            Gauge metrics require the (time: avg, space: avg) aggregation.
            Additional time & space combinations are also available:

            - time: avg, space: avg
            - time: avg, space: max
            - time: avg, space: min
            - time: avg, space: sum
            - time: count, space: sum
            - time: max, space: max
            - time: min, space: min
            - time: sum, space: avg
            - time: sum, space: sum

            Can only be applied to metrics that have a `metric_type` of `count`, `rate`, or `gauge`.
        :type aggregations: MetricCustomAggregations, optional

        :param include_percentiles: Toggle to include/exclude percentiles for a distribution metric.
            Defaults to false. Can only be applied to metrics that have a `metric_type` of `distribution`.
        :type include_percentiles: bool, optional

        :param metric_type: The metric's type.
        :type metric_type: MetricTagConfigurationMetricTypes

        :param tags: A list of tag keys that will be queryable for your metric.
        :type tags: [str]
        """
        super().__init__(kwargs)
        tags = kwargs.get("tags", [])

        self._check_pos_args(args)

        self.metric_type = metric_type
        self.tags = tags

    @classmethod
    def _from_openapi_data(cls, metric_type, *args, **kwargs):
        """Helper creating a new instance from a response."""
        tags = kwargs.get("tags", [])

        self = super(MetricTagConfigurationCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.metric_type = metric_type
        self.tags = tags
        return self
