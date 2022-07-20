# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DistributionPointsSeries(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.distribution_point import DistributionPoint
        from datadog_api_client.v1.model.distribution_points_type import DistributionPointsType

        return {
            "host": (str,),
            "metric": (str,),
            "points": ([DistributionPoint],),
            "tags": ([str],),
            "type": (DistributionPointsType,),
        }

    attribute_map = {
        "host": "host",
        "metric": "metric",
        "points": "points",
        "tags": "tags",
        "type": "type",
    }

    def __init__(self, metric, points, *args, **kwargs):
        """
        A distribution points metric to submit to Datadog.

        :param host: The name of the host that produced the distribution point metric.
        :type host: str, optional

        :param metric: The name of the distribution points metric.
        :type metric: str

        :param points: Points relating to the distribution point metric. All points must be tuples with timestamp and a list of values (cannot be a string). Timestamps should be in POSIX time in seconds.
        :type points: [DistributionPoint]

        :param tags: A list of tags associated with the distribution point metric.
        :type tags: [str], optional

        :param type: The type of the distribution point.
        :type type: DistributionPointsType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.metric = metric
        self.points = points

    @classmethod
    def _from_openapi_data(cls, metric, points, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DistributionPointsSeries, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.metric = metric
        self.points = points
        return self
