# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsMetricCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_metric_compute_aggregation_type import LogsMetricComputeAggregationType

        return {
            "aggregation_type": (LogsMetricComputeAggregationType,),
            "path": (str,),
        }

    attribute_map = {
        "aggregation_type": "aggregation_type",
        "path": "path",
    }

    def __init__(self, aggregation_type, *args, **kwargs):
        """
        The compute rule to compute the log-based metric.

        :param aggregation_type: The type of aggregation to use.
        :type aggregation_type: LogsMetricComputeAggregationType

        :param path: The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution").
        :type path: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.aggregation_type = aggregation_type

    @classmethod
    def _from_openapi_data(cls, aggregation_type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsMetricCompute, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.aggregation_type = aggregation_type
        return self
