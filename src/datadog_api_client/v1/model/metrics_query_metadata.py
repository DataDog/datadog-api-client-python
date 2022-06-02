# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class MetricsQueryMetadata(ModelNormal):
    validations = {
        "unit": {
            "max_items": 2,
            "min_items": 2,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.point import Point
        from datadog_api_client.v1.model.metrics_query_unit import MetricsQueryUnit

        return {
            "aggr": (str, none_type),
            "display_name": (str,),
            "end": (int,),
            "expression": (str,),
            "interval": (int,),
            "length": (int,),
            "metric": (str,),
            "pointlist": ([Point],),
            "query_index": (int,),
            "scope": (str,),
            "start": (int,),
            "tag_set": ([str],),
            "unit": ([MetricsQueryUnit],),
        }

    attribute_map = {
        "aggr": "aggr",
        "display_name": "display_name",
        "end": "end",
        "expression": "expression",
        "interval": "interval",
        "length": "length",
        "metric": "metric",
        "pointlist": "pointlist",
        "query_index": "query_index",
        "scope": "scope",
        "start": "start",
        "tag_set": "tag_set",
        "unit": "unit",
    }
    read_only_vars = {
        "aggr",
        "display_name",
        "end",
        "expression",
        "interval",
        "length",
        "metric",
        "pointlist",
        "query_index",
        "scope",
        "start",
        "tag_set",
        "unit",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing all metric names returned and their associated metadata.

        :param aggr: Aggregation type.
        :type aggr: str, none_type, optional

        :param display_name: Display name of the metric.
        :type display_name: str, optional

        :param end: End of the time window, milliseconds since Unix epoch.
        :type end: int, optional

        :param expression: Metric expression.
        :type expression: str, optional

        :param interval: Number of seconds between data samples.
        :type interval: int, optional

        :param length: Number of data samples.
        :type length: int, optional

        :param metric: Metric name.
        :type metric: str, optional

        :param pointlist: List of points of the time series.
        :type pointlist: [Point], optional

        :param query_index: The index of the series' query within the request.
        :type query_index: int, optional

        :param scope: Metric scope, comma separated list of tags.
        :type scope: str, optional

        :param start: Start of the time window, milliseconds since Unix epoch.
        :type start: int, optional

        :param tag_set: Unique tags identifying this series.
        :type tag_set: [str], optional

        :param unit: Detailed information about the metric unit.
            First element describes the "primary unit" (for example, ``bytes`` in ``bytes per second`` ),
            second describes the "per unit" (for example, ``second`` in ``bytes per second`` ).
        :type unit: [MetricsQueryUnit], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricsQueryMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
