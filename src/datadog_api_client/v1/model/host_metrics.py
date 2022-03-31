# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HostMetrics(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cpu": (float,),
            "iowait": (float,),
            "load": (float,),
        }

    attribute_map = {
        "cpu": "cpu",
        "iowait": "iowait",
        "load": "load",
    }

    def __init__(self, *args, **kwargs):
        """
        Host Metrics collected.

        :param cpu: The percent of CPU used (everything but idle).
        :type cpu: float, optional

        :param iowait: The percent of CPU spent waiting on the IO (not reported for all platforms).
        :type iowait: float, optional

        :param load: The system load over the last 15 minutes.
        :type load: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostMetrics, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
