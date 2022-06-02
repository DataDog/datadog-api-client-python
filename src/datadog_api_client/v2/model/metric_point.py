# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricPoint(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "timestamp": (int,),
            "value": (float,),
        }

    attribute_map = {
        "timestamp": "timestamp",
        "value": "value",
    }

    def __init__(self, *args, **kwargs):
        """
        A point object is of the form ``{POSIX_timestamp, numeric_value}``.

        :param timestamp: The timestamp should be in seconds and current.
            Current is defined as not more than 10 minutes in the future or more than 1 hour in the past.
        :type timestamp: int, optional

        :param value: The numeric value format should be a 64bit float gauge-type value.
        :type value: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricPoint, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
