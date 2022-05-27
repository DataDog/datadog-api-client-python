# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsMetricResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_response_compute import LogsMetricResponseCompute
        from datadog_api_client.v2.model.logs_metric_response_filter import LogsMetricResponseFilter
        from datadog_api_client.v2.model.logs_metric_response_group_by import LogsMetricResponseGroupBy

        return {
            "compute": (LogsMetricResponseCompute,),
            "filter": (LogsMetricResponseFilter,),
            "group_by": ([LogsMetricResponseGroupBy],),
        }

    attribute_map = {
        "compute": "compute",
        "filter": "filter",
        "group_by": "group_by",
    }

    def __init__(self, *args, **kwargs):
        """
        The object describing a Datadog log-based metric.

        :param compute: The compute rule to compute the log-based metric.
        :type compute: LogsMetricResponseCompute, optional

        :param filter: The log-based metric filter. Logs matching this filter will be aggregated in this metric.
        :type filter: LogsMetricResponseFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [LogsMetricResponseGroupBy], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsMetricResponseAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
