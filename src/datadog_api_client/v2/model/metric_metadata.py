# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_origin import MetricOrigin

        return {
            "origin": (MetricOrigin,),
        }

    attribute_map = {
        "origin": "origin",
    }

    def __init__(self, *args, **kwargs):
        """
        Metadata for the metric.

        :param origin: Metric origin information.
        :type origin: MetricOrigin, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
