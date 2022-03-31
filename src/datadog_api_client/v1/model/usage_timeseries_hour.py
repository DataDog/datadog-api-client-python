# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageTimeseriesHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hour": (datetime,),
            "num_custom_input_timeseries": (int,),
            "num_custom_output_timeseries": (int,),
            "num_custom_timeseries": (int,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "hour": "hour",
        "num_custom_input_timeseries": "num_custom_input_timeseries",
        "num_custom_output_timeseries": "num_custom_output_timeseries",
        "num_custom_timeseries": "num_custom_timeseries",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        The hourly usage of timeseries.

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param num_custom_input_timeseries: Contains the number of custom metrics that are inputs for aggregations (metric configured is custom).
        :type num_custom_input_timeseries: int, optional

        :param num_custom_output_timeseries: Contains the number of custom metrics that are outputs for aggregations (metric configured is custom).
        :type num_custom_output_timeseries: int, optional

        :param num_custom_timeseries: Contains sum of non-aggregation custom metrics and custom metrics that are outputs for aggregations.
        :type num_custom_timeseries: int, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageTimeseriesHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
