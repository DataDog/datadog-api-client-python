# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class UsageTimeSeriesObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "timestamp": (datetime,),
            "value": (int, none_type),
        }

    attribute_map = {
        "timestamp": "timestamp",
        "value": "value",
    }

    def __init__(self, *args, **kwargs):
        """
        Usage timeseries data.

        :param timestamp: Datetime in ISO-8601 format, UTC. The hour for the usage.
        :type timestamp: datetime, optional

        :param value: Contains the number measured for the given usage_type during the hour.
        :type value: int, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageTimeSeriesObject, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
