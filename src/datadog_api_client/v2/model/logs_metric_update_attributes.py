# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsMetricUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
        from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy

        return {
            "filter": (LogsMetricFilter,),
            "group_by": ([LogsMetricGroupBy],),
        }

    attribute_map = {
        "filter": "filter",
        "group_by": "group_by",
    }

    def __init__(self_, *args, **kwargs):
        """
        The log-based metric properties that will be updated.

        :param filter: The log-based metric filter. Logs matching this filter will be aggregated in this metric.
        :type filter: LogsMetricFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [LogsMetricGroupBy], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
