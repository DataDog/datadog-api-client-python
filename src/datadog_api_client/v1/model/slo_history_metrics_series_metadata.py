# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class SLOHistoryMetricsSeriesMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_history_metrics_series_metadata_unit import (
            SLOHistoryMetricsSeriesMetadataUnit,
        )

        return {
            "aggr": (str,),
            "expression": (str,),
            "metric": (str,),
            "query_index": (int,),
            "scope": (str,),
            "unit": ([SLOHistoryMetricsSeriesMetadataUnit], none_type),
        }

    attribute_map = {
        "aggr": "aggr",
        "expression": "expression",
        "metric": "metric",
        "query_index": "query_index",
        "scope": "scope",
        "unit": "unit",
    }

    def __init__(self, *args, **kwargs):
        """
        Query metadata.

        :param aggr: Query aggregator function.
        :type aggr: str, optional

        :param expression: Query expression.
        :type expression: str, optional

        :param metric: Query metric used.
        :type metric: str, optional

        :param query_index: Query index from original combined query.
        :type query_index: int, optional

        :param scope: Query scope.
        :type scope: str, optional

        :param unit: An array of metric units that contains up to two unit objects.
            For example, bytes represents one unit object and bytes per second represents two unit objects.
            If a metric query only has one unit object, the second array element is null.
        :type unit: [SLOHistoryMetricsSeriesMetadataUnit], none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryMetricsSeriesMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
