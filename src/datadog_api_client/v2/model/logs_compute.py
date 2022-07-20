# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_aggregation_function import LogsAggregationFunction
        from datadog_api_client.v2.model.logs_compute_type import LogsComputeType

        return {
            "aggregation": (LogsAggregationFunction,),
            "interval": (str,),
            "metric": (str,),
            "type": (LogsComputeType,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "type": "type",
    }

    def __init__(self, aggregation, *args, **kwargs):
        """
        A compute rule to compute metrics or timeseries

        :param aggregation: An aggregation function
        :type aggregation: LogsAggregationFunction

        :param interval: The time buckets' size (only used for type=timeseries)
            Defaults to a resolution of 150 points
        :type interval: str, optional

        :param metric: The metric to use
        :type metric: str, optional

        :param type: The type of compute
        :type type: LogsComputeType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation

    @classmethod
    def _from_openapi_data(cls, aggregation, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsCompute, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation
        return self
