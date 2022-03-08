# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (str,),
            "metrics": ([str],),
        }

    attribute_map = {
        "_from": "from",
        "metrics": "metrics",
    }

    def __init__(self, *args, **kwargs):
        """
        Object listing all metric names stored by Datadog since a given time.

        :param _from: Time when the metrics were active, seconds since the Unix epoch.
        :type _from: str, optional

        :param metrics: List of metric names.
        :type metrics: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricsListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
