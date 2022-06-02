# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageTopAvgMetricsHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_metric_category import UsageMetricCategory

        return {
            "avg_metric_hour": (int,),
            "max_metric_hour": (int,),
            "metric_category": (UsageMetricCategory,),
            "metric_name": (str,),
        }

    attribute_map = {
        "avg_metric_hour": "avg_metric_hour",
        "max_metric_hour": "max_metric_hour",
        "metric_category": "metric_category",
        "metric_name": "metric_name",
    }

    def __init__(self, *args, **kwargs):
        """
        Number of hourly recorded custom metrics for a given organization.

        :param avg_metric_hour: Average number of timeseries per hour in which the metric occurs.
        :type avg_metric_hour: int, optional

        :param max_metric_hour: Maximum number of timeseries per hour in which the metric occurs.
        :type max_metric_hour: int, optional

        :param metric_category: Contains the metric category.
        :type metric_category: UsageMetricCategory, optional

        :param metric_name: Contains the custom metric name.
        :type metric_name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageTopAvgMetricsHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
