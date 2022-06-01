# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOHistoryMetricsSeries(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_history_metrics_series_metadata import SLOHistoryMetricsSeriesMetadata

        return {
            "count": (int,),
            "metadata": (SLOHistoryMetricsSeriesMetadata,),
            "sum": (float,),
            "values": ([float],),
        }

    attribute_map = {
        "count": "count",
        "metadata": "metadata",
        "sum": "sum",
        "values": "values",
    }

    def __init__(self, count, sum, values, *args, **kwargs):
        """
        A representation of ``metric`` based SLO time series for the provided queries.
        This is the same response type from ``batch_query`` endpoint.

        :param count: Count of submitted metrics.
        :type count: int

        :param metadata: Query metadata.
        :type metadata: SLOHistoryMetricsSeriesMetadata, optional

        :param sum: Total sum of the query.
        :type sum: float

        :param values: The query values for each metric.
        :type values: [float]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.count = count
        self.sum = sum
        self.values = values

    @classmethod
    def _from_openapi_data(cls, count, sum, values, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryMetricsSeries, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.count = count
        self.sum = sum
        self.values = values
        return self
