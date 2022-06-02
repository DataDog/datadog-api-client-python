# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class Series(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.point import Point

        return {
            "host": (str,),
            "interval": (int, none_type),
            "metric": (str,),
            "points": ([Point],),
            "tags": ([str],),
            "type": (str,),
        }

    attribute_map = {
        "host": "host",
        "interval": "interval",
        "metric": "metric",
        "points": "points",
        "tags": "tags",
        "type": "type",
    }

    def __init__(self, metric, points, *args, **kwargs):
        """
        A metric to submit to Datadog.
        See `Datadog metrics <https://docs.datadoghq.com/developers/metrics/#custom-metrics-properties>`_.

        :param host: The name of the host that produced the metric.
        :type host: str, optional

        :param interval: If the type of the metric is rate or count, define the corresponding interval.
        :type interval: int, none_type, optional

        :param metric: The name of the timeseries.
        :type metric: str

        :param points: Points relating to a metric. All points must be tuples with timestamp and a scalar value (cannot be a string). Timestamps should be in POSIX time in seconds, and cannot be more than ten minutes in the future or more than one hour in the past.
        :type points: [Point]

        :param tags: A list of tags associated with the metric.
        :type tags: [str], optional

        :param type: The type of the metric. Valid types are "", ``count`` , ``gauge`` , and ``rate``.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.metric = metric
        self.points = points

    @classmethod
    def _from_openapi_data(cls, metric, points, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Series, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.metric = metric
        self.points = points
        return self
