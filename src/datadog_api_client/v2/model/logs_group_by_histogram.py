# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsGroupByHistogram(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "interval": (float,),
            "max": (float,),
            "min": (float,),
        }

    attribute_map = {
        "interval": "interval",
        "max": "max",
        "min": "min",
    }

    def __init__(self, interval, max, min, *args, **kwargs):
        """
        Used to perform a histogram computation (only for measure facets).
        Note: At most 100 buckets are allowed, the number of buckets is (max - min)/interval.

        :param interval: The bin size of the histogram buckets
        :type interval: float

        :param max: The maximum value for the measure used in the histogram
            (values greater than this one are filtered out)
        :type max: float

        :param min: The minimum value for the measure used in the histogram
            (values smaller than this one are filtered out)
        :type min: float
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.interval = interval
        self.max = max
        self.min = min

    @classmethod
    def _from_openapi_data(cls, interval, max, min, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsGroupByHistogram, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.interval = interval
        self.max = max
        self.min = min
        return self
