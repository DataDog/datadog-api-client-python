# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class RUMAggregateBucketValueTimeseriesPoint(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "time": (datetime,),
            "value": (float,),
        }

    attribute_map = {
        "time": "time",
        "value": "value",
    }

    def __init__(self, *args, **kwargs):
        """
        A timeseries point.

        :param time: The time value for this point.
        :type time: datetime, optional

        :param value: The value for this point.
        :type value: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMAggregateBucketValueTimeseriesPoint, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
