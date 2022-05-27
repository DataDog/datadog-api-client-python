# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsMetricCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
        from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
        from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy

        return {
            "compute": (LogsMetricCompute,),
            "filter": (LogsMetricFilter,),
            "group_by": ([LogsMetricGroupBy],),
        }

    attribute_map = {
        "compute": "compute",
        "filter": "filter",
        "group_by": "group_by",
    }

    def __init__(self, compute, *args, **kwargs):
        """
        The object describing the Datadog log-based metric to create.

        :param compute: The compute rule to compute the log-based metric.
        :type compute: LogsMetricCompute

        :param filter: The log-based metric filter. Logs matching this filter will be aggregated in this metric.
        :type filter: LogsMetricFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [LogsMetricGroupBy], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.compute = compute

    @classmethod
    def _from_openapi_data(cls, compute, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsMetricCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.compute = compute
        return self
