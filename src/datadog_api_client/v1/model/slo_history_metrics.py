# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOHistoryMetrics(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_history_metrics_series import SLOHistoryMetricsSeries

        return {
            "denominator": (SLOHistoryMetricsSeries,),
            "interval": (int,),
            "message": (str,),
            "numerator": (SLOHistoryMetricsSeries,),
            "query": (str,),
            "res_type": (str,),
            "resp_version": (int,),
            "times": ([float],),
        }

    attribute_map = {
        "denominator": "denominator",
        "interval": "interval",
        "message": "message",
        "numerator": "numerator",
        "query": "query",
        "res_type": "res_type",
        "resp_version": "resp_version",
        "times": "times",
    }

    def __init__(self, denominator, interval, numerator, query, res_type, resp_version, times, *args, **kwargs):
        """
        A ``metric`` based SLO history response.

        This is not included in responses for ``monitor`` based SLOs.

        :param denominator: A representation of ``metric`` based SLO time series for the provided queries.
            This is the same response type from ``batch_query`` endpoint.
        :type denominator: SLOHistoryMetricsSeries

        :param interval: The aggregated query interval for the series data. It's implicit based on the query time window.
        :type interval: int

        :param message: Optional message if there are specific query issues/warnings.
        :type message: str, optional

        :param numerator: A representation of ``metric`` based SLO time series for the provided queries.
            This is the same response type from ``batch_query`` endpoint.
        :type numerator: SLOHistoryMetricsSeries

        :param query: The combined numerator and denominator query CSV.
        :type query: str

        :param res_type: The series result type. This mimics ``batch_query`` response type.
        :type res_type: str

        :param resp_version: The series response version type. This mimics ``batch_query`` response type.
        :type resp_version: int

        :param times: An array of query timestamps in EPOCH milliseconds.
        :type times: [float]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.denominator = denominator
        self.interval = interval
        self.numerator = numerator
        self.query = query
        self.res_type = res_type
        self.resp_version = resp_version
        self.times = times

    @classmethod
    def _from_openapi_data(
        cls, denominator, interval, numerator, query, res_type, resp_version, times, *args, **kwargs
    ):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryMetrics, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.denominator = denominator
        self.interval = interval
        self.numerator = numerator
        self.query = query
        self.res_type = res_type
        self.resp_version = resp_version
        self.times = times
        return self
