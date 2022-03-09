# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsQueryCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "facet": (str,),
            "interval": (int,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "facet": "facet",
        "interval": "interval",
    }

    def __init__(self, aggregation, *args, **kwargs):
        """
        Define computation for a log query.

        :param aggregation: The aggregation method.
        :type aggregation: str

        :param facet: Facet name.
        :type facet: str, optional

        :param interval: Define a time interval in seconds.
        :type interval: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation

    @classmethod
    def _from_openapi_data(cls, aggregation, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsQueryCompute, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation
        return self
