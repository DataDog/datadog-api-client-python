# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
    from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes

    globals()["MetricCustomAggregations"] = MetricCustomAggregations
    globals()["MetricTagConfigurationMetricTypes"] = MetricTagConfigurationMetricTypes


class MetricTagConfigurationCreateAttributes(ModelNormal):
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
            "include_percentiles": (bool,),
            "metric_type": (MetricTagConfigurationMetricTypes,),
            "tags": ([str],),
        }

    attribute_map = {
        "metric_type": "metric_type",
        "tags": "tags",
        "aggregations": "aggregations",
        "include_percentiles": "include_percentiles",
    }

    read_only_vars = {}

    def __init__(self, metric_type, *args, **kwargs):
        """MetricTagConfigurationCreateAttributes - a model defined in OpenAPI

        Args:
            metric_type (MetricTagConfigurationMetricTypes):

        Keyword Args:
            tags ([str]): A list of tag keys that will be queryable for your metric. Defaults to [].
            aggregations (MetricCustomAggregations): [optional]
            include_percentiles (bool): [optional] Toggle to include/exclude percentiles for a distribution metric. Defaults to false. Can only be applied to metrics that have a `metric_type` of `distribution`. If omitted the server will use the default value of False.
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
