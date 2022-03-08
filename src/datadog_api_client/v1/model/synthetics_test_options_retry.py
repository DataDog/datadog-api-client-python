# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestOptionsRetry(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "interval": (float,),
        }

    attribute_map = {
        "count": "count",
        "interval": "interval",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing the retry strategy to apply to a Synthetic test.

        :param count: Number of times a test needs to be retried before marking a
            location as failed. Defaults to 0.
        :type count: int, optional

        :param interval: Time interval between retries (in milliseconds). Defaults to
            300ms.
        :type interval: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestOptionsRetry, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
