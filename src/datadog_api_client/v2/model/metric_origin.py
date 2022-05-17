# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricOrigin(ModelNormal):
    validations = {
        "metric_type": {
            "inclusive_maximum": 1000,
        },
        "product": {
            "inclusive_maximum": 1000,
        },
        "service": {
            "inclusive_maximum": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "metric_type": (int,),
            "product": (int,),
            "service": (int,),
        }

    attribute_map = {
        "metric_type": "metric_type",
        "product": "product",
        "service": "service",
    }

    def __init__(self, *args, **kwargs):
        """
        Metric origin information.

        :param metric_type: The origin metric type code
        :type metric_type: int, optional

        :param product: The origin product code
        :type product: int, optional

        :param service: The origin service code
        :type service: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricOrigin, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
