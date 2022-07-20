# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricCustomAggregation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_custom_space_aggregation import MetricCustomSpaceAggregation
        from datadog_api_client.v2.model.metric_custom_time_aggregation import MetricCustomTimeAggregation

        return {
            "space": (MetricCustomSpaceAggregation,),
            "time": (MetricCustomTimeAggregation,),
        }

    attribute_map = {
        "space": "space",
        "time": "time",
    }

    def __init__(self, space, time, *args, **kwargs):
        """
        A time and space aggregation combination for use in query.

        :param space: A space aggregation for use in query.
        :type space: MetricCustomSpaceAggregation

        :param time: A time aggregation for use in query.
        :type time: MetricCustomTimeAggregation
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.space = space
        self.time = time

    @classmethod
    def _from_openapi_data(cls, space, time, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricCustomAggregation, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.space = space
        self.time = time
        return self
