# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricDistinctVolumeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "distinct_volume": (int,),
        }

    attribute_map = {
        "distinct_volume": "distinct_volume",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing the definition of a metric's distinct volume.

        :param distinct_volume: Distinct volume for the given metric.
        :type distinct_volume: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricDistinctVolumeAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
