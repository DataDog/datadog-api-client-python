# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestOptionsMonitorOptions(ModelNormal):

    validations = {
        "renotify_interval": {
            "inclusive_maximum": 1440,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types():
        return {
            "renotify_interval": (int,),
        }

    attribute_map = {
        "renotify_interval": "renotify_interval",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object containing the options for a Synthetic test as a monitor
        (for example, renotification).

        :param renotify_interval: Time interval before renotifying if the test is still failing
            (in minutes).
        :type renotify_interval: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestOptionsMonitorOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
