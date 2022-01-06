# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
    from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

    globals()["MetricCustomAggregations"] = MetricCustomAggregations
    globals()["MetricTagConfigurationMetricTypes"] = MetricTagConfigurationMetricTypes


class MetricTagConfigurationAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
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

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """MetricTagConfigurationAttributes - a model defined in OpenAPI

        Keyword Args:
            aggregations (MetricCustomAggregations): [optional]
            created_at (datetime): [optional] Timestamp when the tag configuration was created.
            include_percentiles (bool): [optional] Toggle to turn on/off percentile aggregations for distribution metrics. Only present when the `metric_type` is `distribution`.
            metric_type (MetricTagConfigurationMetricTypes): [optional]
            modified_at (datetime): [optional] Timestamp when the tag configuration was last modified.
            tags ([str]): [optional] List of tag keys on which to group.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricTagConfigurationAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
