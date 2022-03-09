# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorOptionsAggregation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "group_by": (str,),
            "metric": (str,),
            "type": (str,),
        }

    attribute_map = {
        "group_by": "group_by",
        "metric": "metric",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Type of aggregation performed in the monitor query.

        :param group_by: Group to break down the monitor on.
        :type group_by: str, optional

        :param metric: Metric name used in the monitor.
        :type metric: str, optional

        :param type: Metric type used in the monitor.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorOptionsAggregation, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
